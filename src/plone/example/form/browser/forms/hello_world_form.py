from plone.z3cform.layout import wrap_form
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema import TextLine


_ = MessageFactory("hello_world")


class IHelloWorldForm(Interface):

    hello_world_name = TextLine(
        title=_(u"Name"), description=_(u"Please enter your name."), required=False
    )


class HelloWorldForm(form.Form):

    fields = field.Fields(IHelloWorldForm)
    ignoreContext = True

    def updateWidgets(self):
        super(HelloWorldForm, self).updateWidgets()

    @button.buttonAndHandler(u"Save")
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            return False

        if data["hello_world_name"] is not None:
            hello_name = data["hello_world_name"]
        else:
            hello_name = "World"

        IStatusMessage(self.request).addStatusMessage("Hello %s" % hello_name, "info")
        redirect_url = "%s/@@hello_world_form" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)

    @button.buttonAndHandler(u"Cancel")
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage("Hello No One", "info")
        redirect_url = "%s/@@hello_world_form" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)


HelloWorldFormView = wrap_form(HelloWorldForm)
