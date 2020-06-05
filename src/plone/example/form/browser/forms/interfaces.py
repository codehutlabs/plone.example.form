from plone.autoform import directives
from plone.formwidget.recaptcha.widget import ReCaptchaFieldWidget
from plone.supermodel import model
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface


_ = MessageFactory("hello_world")


class IPizzaOrderFormMarker(Interface):
    pass


class IPizzaOrderForm(model.Schema):
    # Check: https://docs.plone.org/develop/addons/schema-driven-forms/creating-a-simple-form/creating-a-schema.html
    # and here: https://docs.plone.org/develop/addons/schema-driven-forms/customising-form-behaviour/fieldsets.html

    name = schema.TextLine(title=_(u"Your full name"), required=True)

    telephone = schema.ASCIILine(
        title=_(u"Telephone number"),
        description=_(u"We prefer a mobile number"),
        required=False,
    )

    # model.fieldset(
    #     'order123',
    #     label=_(u"Order 123"),
    #     fields=['address1', 'address2', 'postcode', 'orderItems', 'captcha']
    # )

    address1 = schema.TextLine(title=_(u"Address line 1"), required=False)

    address2 = schema.TextLine(title=_(u"Address line 2"), required=False)

    postcode = schema.TextLine(title=_(u"Postcode"), required=False)

    orderItems = schema.Set(
        title=_(u"Your order"),
        value_type=schema.Choice(
            values=[_(u"Margherita"), _(u"Pepperoni"), _(u"Hawaiian")]
        ),
        required=True,
    )

    directives.widget('captcha', ReCaptchaFieldWidget)
    captcha = schema.TextLine(title=_(u"ReCaptcha"), required=False)
