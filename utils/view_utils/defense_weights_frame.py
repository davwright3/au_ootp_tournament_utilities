"""Frame for user to set defense weights."""
import customtkinter as ctk


class DefenseWeightsFrame(ctk.CTkFrame):
    """Frame class for defense weights."""

    def __init__(self, parent):
        """Initialize the frame."""
        ctk.CTkFrame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        # Variables
        self.catch_abil_var = ctk.StringVar(value='1')
        self.catch_frame_var = ctk.StringVar(value='1')
        self.catch_arm_var = ctk.StringVar(value='1')
        self.infield_range_var = ctk.StringVar(value='1')
        self.infield_error_var = ctk.StringVar(value='1')
        self.infield_arm_var = ctk.StringVar(value='1')
        self.infield_dp_var = ctk.StringVar(value='1')
        self.outfield_range_var = ctk.StringVar(value='1')
        self.outfield_error_var = ctk.StringVar(value='1')
        self.outfield_arm_var = ctk.StringVar(value='1')

        # Frame label
        self.frame_label = ctk.CTkLabel(
            self,
            text="Defense Weights",
        )
        self.frame_label.grid(row=0, column=0, columnspan=5, sticky='nsew')

        # Side labels
        self.catcher_label = ctk.CTkLabel(
            self,
            text='Catcher'
        )
        self.catcher_label.grid(row=2, column=0, sticky='nsew')

        self.infield_label = ctk.CTkLabel(
            self,
            text='IF'
        )
        self.infield_label.grid(row=4, column=0, sticky='nsew')

        self.outfield_label = ctk.CTkLabel(
            self,
            text='OF'
        )
        self.outfield_label.grid(row=5, column=0, sticky='nsew')

        # Top labels
        self.catcher_abil_label = ctk.CTkLabel(
            self,
            text='Abil'
        )
        self.catcher_abil_label.grid(row=1, column=1, sticky='nsew')

        self.catcher_frame_label = ctk.CTkLabel(
            self,
            text='Frame'
        )
        self.catcher_frame_label.grid(row=1, column=2, sticky='nsew')

        self.catch_arm_label = ctk.CTkLabel(
            self,
            text='Arm'
        )
        self.catch_arm_label.grid(row=1, column=3, sticky='nsew')

        self.range_label = ctk.CTkLabel(
            self,
            text='Range'
        )
        self.range_label.grid(row=3, column=1, sticky='nsew')

        self.error_label = ctk.CTkLabel(
            self,
            text='Error'
        )
        self.error_label.grid(row=3, column=2, sticky='nsew')

        self.arm_label = ctk.CTkLabel(
            self,
            text='Arm'
        )
        self.arm_label.grid(row=3, column=3, sticky='nsew')

        self.turn_dp_label = ctk.CTkLabel(
            self,
            text='DP'
        )
        self.turn_dp_label.grid(row=3, column=4, sticky='nsew')

        # Input boxes
        self.catcher_abil_input = ctk.CTkEntry(
            self,
            textvariable=self.catch_abil_var,
            width=25
        )
        self.catcher_abil_input.grid(row=2, column=1, sticky='nsew')

        self.catch_frame_input = ctk.CTkEntry(
            self,
            textvariable=self.catch_frame_var,
            width=25
        )
        self.catch_frame_input.grid(row=2, column=2, sticky='nsew')

        self.catcher_arm_input = ctk.CTkEntry(
            self,
            textvariable=self.catch_arm_var,
            width=25
        )
        self.catcher_arm_input.grid(row=2, column=3, sticky='nsew')

        self.infield_range_input = ctk.CTkEntry(
            self,
            textvariable=self.infield_range_var,
            width=25
        )
        self.infield_range_input.grid(row=4, column=1, sticky='nsew')

        self.infield_error_input = ctk.CTkEntry(
            self,
            textvariable=self.infield_error_var,
            width=25
        )
        self.infield_error_input.grid(row=4, column=2, sticky='nsew')

        self.infield_arm_input = ctk.CTkEntry(
            self,
            textvariable=self.infield_arm_var,
            width=25
        )
        self.infield_arm_input.grid(row=4, column=3, sticky='nsew')

        self.turn_dp_input = ctk.CTkEntry(
            self,
            textvariable=self.infield_dp_var,
            width=25
        )
        self.turn_dp_input.grid(row=4, column=4, sticky='nsew')

        self.outfield_range_input = ctk.CTkEntry(
            self,
            textvariable=self.outfield_range_var,
            width=25
        )
        self.outfield_range_input.grid(row=5, column=1, sticky='nsew')

        self.outfield_error_input = ctk.CTkEntry(
            self,
            textvariable=self.outfield_error_var,
            width=25
        )
        self.outfield_error_input.grid(row=5, column=2, sticky='nsew')

        self.outfield_arm_input = ctk.CTkEntry(
            self,
            textvariable=self.outfield_arm_var,
            width=25
        )
        self.outfield_arm_input.grid(row=5, column=3, sticky='nsew')

    def get_defense_weights(self):
        """Get the weights for defense used in other scripts."""
        defense_weights = {}

        def parse(var):
            try:
                return float(var.get())
            except ValueError:
                return 1

        defense_weights['CatchAbil'] = parse(self.catch_abil_var)
        defense_weights['CatchFrame'] = parse(self.catch_frame_var)
        defense_weights['CatchArm'] = parse(self.catch_arm_var)
        defense_weights['IF Range'] = parse(self.infield_range_var)
        defense_weights['IF Error'] = parse(self.infield_error_var)
        defense_weights['IF Arm'] = parse(self.infield_arm_var)
        defense_weights['DP'] = parse(self.infield_dp_var)
        defense_weights['OF Range'] = parse(self.outfield_range_var)
        defense_weights['OF Error'] = parse(self.outfield_error_var)
        defense_weights['OF Arm'] = parse(self.outfield_arm_var)

        return defense_weights
