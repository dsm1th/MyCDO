# To change this template, choose Tools | Templates
# and open the template in the editor.
import puremvc.patterns.facade
import puremvc.patterns.proxy
import puremvc.patterns.command
import puremvc.interfaces

__author__="darrensmith"
__date__ ="$Sep 6, 2011 4:07:33 PM$"

class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
	def execute(self,note):
		self.facade.registerProxy(model.UserProxy())
		self.facade.registerProxy(model.RoleProxy())

		mainPanel = note.getBody()
		self.facade.registerMediator(view.DialogMediator(mainPanel))
		self.facade.registerMediator(view.UserFormMediator(mainPanel.userForm))
		self.facade.registerMediator(view.UserListMediator(mainPanel.userList))
		self.facade.registerMediator(view.RolePanelMediator(mainPanel.rolePanel))

class AddRoleResultCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
	def execute(self,note):
		result = note.getBody()
		if not result:
			self.facade.sendNotification(main.AppFacade.SHOW_DIALOG, "Role already exists for this user.")

class DeleteUserCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
	def execute(self,note):
           user = note.getBody()
           userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
           roleProxy = self.facade.retrieveProxy(model.RoleProxy.NAME)
           userProxy.deleteItem(user)
           roleProxy.deleteItem(user)
           self.facade.sendNotification(main.AppFacade.USER_DELETED)


class AppFacade(puremvc.patterns.facade.Facade):
	
	STARTUP             = "startup"
	TRANSFER_FUNDS      = "transferFunds"
	REVERSE_OC_TEST     = "reverseOCTest"
	REVERSE_IC_TEST     = "reverseICTest"
        REINVEST_SHIFTED    = "reinvestShifted"
        REINVEST_PRORATA    = "reinvestProRata"
        REINVEST_FIXED_RATIO="reinvestFixedRatio"
        REINVEST            = "revinest"
        PAY_RESIDUAL        = "payResidual"
        PAY_RESIDUAL_PRORATA="payResidualProRata"
        PAY_PRINCIPAL       ="payPrincipal"
        PAY_PRINCIPAL_SEQ   ="payPrincipalSequential"
        PAY_PRINCIPAL_PR    ="payPrincipalProRata"
        PAY_PRINCIPAL_AREAS

	USER_SELECTED     = "userSelected"
	USER_ADDED        = "userAdded"
	USER_UPDATED      = "userUpdated"
	USER_DELETED      = "userDeleted"

	ADD_ROLE          = "addRole"
	ADD_ROLE_RESULT   = "addRoleResult"
	
	SHOW_DIALOG       =  "showDialog"
	
	
	def __init__(self):
		self.initializeFacade()
		
	@staticmethod
	def getInstance():
		return AppFacade()
		
	def initializeFacade(self):
		super(AppFacade, self).initializeFacade()
	
		self.initializeController()
   
	def initializeController(self):
		super(AppFacade, self).initializeController()
		
		super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)
		super(AppFacade, self).registerCommand(AppFacade.DELETE_USER, controller.DeleteUserCommand)
		super(AppFacade, self).registerCommand(AppFacade.ADD_ROLE_RESULT, controller.AddRoleResultCommand)


if __name__ == "__main__":
    print "Hello World"
