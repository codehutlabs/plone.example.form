from Acquisition import aq_inner
from plone import api
from plone.autoform.form import AutoExtensibleForm
from plone.example.form.browser.forms.interfaces import IPizzaOrderForm
from plone.formwidget.recaptcha.widget import ReCaptchaFieldWidget
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import form
from z3c.form import group
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer
from zope.interface import Interface

import logging


_ = MessageFactory("hello_world")
logger = logging.getLogger(__name__)


@implementer(IPizzaOrderForm)
@adapter(Interface)
class PizzaOrderFormAdapter(object):
    def __init__(self, context):
        self.name = None
        self.address1 = None
        self.address2 = None
        self.postcode = None
        self.telephone = None
        self.orderItems = None


class PizzaOrderForm(AutoExtensibleForm, group.GroupForm, form.Form):

    enableCSRFProtection = True
    enable_form_tabbing = False

    schema = IPizzaOrderForm
    form_name = "order_form"

    label = _(u"Order your pizza")
    description = _(u"We will contact you to confirm your order and delivery.")

    def update(self):
        # disable Plone's editable border
        self.request.set("disable_border", True)

        # call the base class version - this is very important!
        super(PizzaOrderForm, self).update()

    # def updateWidgets(self):
    #     self.fields["captcha"].widgetFactory = ReCaptchaFieldWidget
    #
    #     # call the base class version - this is very important!
    #     super(PizzaOrderForm, self).updateWidgets()

    @button.buttonAndHandler(_(u"Order"))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        # Handle order here. For now, just print it to the console. A more
        # realistic action would be to send the order to another system, send
        # an email, or similar

        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="recaptcha"
        )

        if captcha.verify():
            logger.info("ReCaptcha validation passed.")
        else:
            logger.info("The code you entered was wrong, please enter the new one.")

        body = "Order received:\n"
        body = "{}  Customer: {}\n".format(body, data["name"])
        body = "{}  Phone:    {}\n".format(body, data["telephone"])
        body = "{}  Address:  {}\n".format(body, data["address1"])
        body = "{}            {}\n".format(body, data["address2"])
        body = "{}            {}\n".format(body, data["postcode"])
        body = "{}  Order:    {}\n".format(body, ", ".join(data["orderItems"]))

        recipient = "info@plone.example.form"
        sender = "plone@plone.example.form"
        subject = "Order received"
        immediate = True

        api.portal.send_email(
            sender=sender,
            recipient=recipient,
            subject=subject,
            body=body,
            immediate=immediate,
        )

        # Redirect back to the front page with a status message

        IStatusMessage(self.request).addStatusMessage(
            _(u"Thank you for your order. We will contact you shortly"), "info"
        )

        context_url = self.context.absolute_url()
        redirect_url = "{}/@@pizza_order_form".format(context_url)
        self.request.response.redirect(redirect_url)

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page.
        """
        contextURL = self.context.absolute_url()
        self.request.response.redirect(contextURL)
