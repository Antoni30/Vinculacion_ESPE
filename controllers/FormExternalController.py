from core.Controller import Controller
class FormExternalController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.formExternal = self.loadView("formExternal")

    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    """
        @Override
    """
    def main(self):
        self.formExternal.main()