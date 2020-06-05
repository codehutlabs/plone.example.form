from plone.autoform.form import AutoExtensibleForm
from plone.example.form.browser.forms.interfaces import IPizzaOrderForm
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import form
from zope.component import adapter
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer
from zope.interface import Interface


_ = MessageFactory("hello_world")


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


class PizzaOrderForm(AutoExtensibleForm, form.Form):

    enableCSRFProtection = True

    schema = IPizzaOrderForm
    form_name = "order_form"

    label = _(u"Order your pizza")
    description = _(u"We will contact you to confirm your order and delivery.")

    def update(self):
        # disable Plone's editable border
        self.request.set("disable_border", True)

        # call the base class version - this is very important!
        super(PizzaOrderForm, self).update()

    @button.buttonAndHandler(_(u"Order"))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        # Handle order here. For now, just print it to the console. A more
        # realistic action would be to send the order to another system, send
        # an email, or similar

        print(u"Order received:")
        print(u"  Customer: ", data["name"])
        print(u"  Telephone:", data["telephone"])
        print(u"  Address:  ", data["address1"])
        print(u"            ", data["address2"])
        print(u"            ", data["postcode"])
        print(u"  Order:    ", ", ".join(data["orderItems"]))
        print(u"")

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
