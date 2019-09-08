from plone.supermodel import model
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface


_ = MessageFactory("hello_world")


class IPizzaOrderFormMarker(Interface):
    pass


class IPizzaOrderForm(model.Schema):

    name = schema.TextLine(title=_(u"Your full name"), required=True)

    address1 = schema.TextLine(title=_(u"Address line 1"), required=False)

    address2 = schema.TextLine(title=_(u"Address line 2"), required=False)

    postcode = schema.TextLine(title=_(u"Postcode"), required=False)

    telephone = schema.ASCIILine(
        title=_(u"Telephone number"),
        description=_(u"We prefer a mobile number"),
        required=False,
    )

    orderItems = schema.Set(
        title=_(u"Your order"),
        value_type=schema.Choice(
            values=[_(u"Margherita"), _(u"Pepperoni"), _(u"Hawaiian")]
        ),
        required=True,
    )
