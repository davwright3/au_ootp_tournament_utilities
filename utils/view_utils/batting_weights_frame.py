"""Custom frame for users to enter batting weights."""
import customtkinter as ctk


class BattingWeightsFrame(ctk.CTkFrame):
    """Frame for users to enter batting weights."""

    def __init__(self, parent):
        """Frame for users to enter batting weights."""
        ctk.CTkFrame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Variables for the weights
        self.babip_overall_var = ctk.StringVar(value='1')
        self.babip_v_left_var = ctk.StringVar(value='1')
        self.babip_v_right_var = ctk.StringVar(value='1')
        self.avoid_k_overall_var = ctk.StringVar(value='1')
        self.avoid_k_left_var = ctk.StringVar(value='1')
        self.avoid_k_right_var = ctk.StringVar(value='1')
        self.gap_overall_var = ctk.StringVar(value='1')
        self.gap_v_left_var = ctk.StringVar(value='1')
        self.gap_v_right_var = ctk.StringVar(value='1')
        self.power_overall_var = ctk.StringVar(value='1')
        self.power_v_left_var = ctk.StringVar(value='1')
        self.power_v_right_var = ctk.StringVar(value='1')
        self.eye_overall_var = ctk.StringVar(value='1')
        self.eye_v_left_var = ctk.StringVar(value='1')
        self.eye_v_right_var = ctk.StringVar(value='1')

        # Left side labels
        frame_label = ctk.CTkLabel(self, text='Bat Weights')
        frame_label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        babip_label = ctk.CTkLabel(self, text='BABIP')
        babip_label.grid(column=0, row=2, sticky='nsew')

        avoid_k_label = ctk.CTkLabel(self, text='AvK')
        avoid_k_label.grid(column=0, row=3, sticky='nsew')

        gap_label = ctk.CTkLabel(self, text='GAP')
        gap_label.grid(column=0, row=4, sticky='nsew')

        power_label = ctk.CTkLabel(self, text='Power')
        power_label.grid(column=0, row=5, sticky='nsew')

        eye_label = ctk.CTkLabel(self, text='Eye')
        eye_label.grid(column=0, row=6, sticky='nsew')

        # Top labels
        overall_label = ctk.CTkLabel(self, text='OA')
        overall_label.grid(column=1, row=1, sticky='nsew')

        vs_left_label = ctk.CTkLabel(self, text='vsL')
        vs_left_label.grid(column=2, row=1, sticky='nsew')

        vs_right_label = ctk.CTkLabel(self, text='vsR')
        vs_right_label.grid(column=3, row=1, sticky='nsew')

        # User inputs for weights
        babip_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.babip_overall_var,
            width=25
        )
        babip_overall_input.grid(column=1, row=2, sticky='nsew')

        babip_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.babip_v_left_var,
            width=25
        )
        babip_v_left_input.grid(column=2, row=2, sticky='nsew')

        babip_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.babip_v_right_var,
            width=25
        )
        babip_v_right_input.grid(column=3, row=2, sticky='nsew')

        avoid_k_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.avoid_k_overall_var,
            width=25
        )
        avoid_k_overall_input.grid(column=1, row=3, sticky='nsew')

        avoid_k_left_input = ctk.CTkEntry(
            self,
            textvariable=self.avoid_k_left_var,
            width=25
        )
        avoid_k_left_input.grid(column=2, row=3, sticky='nsew')

        avoid_k_right_input = ctk.CTkEntry(
            self,
            textvariable=self.avoid_k_right_var,
            width=25
        )
        avoid_k_right_input.grid(column=3, row=3, sticky='nsew')

        gap_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.gap_overall_var,
            width=25
        )
        gap_overall_input.grid(column=1, row=4, sticky='nsew')

        gap_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.gap_v_left_var,
            width=25
        )
        gap_v_left_input.grid(column=2, row=4, sticky='nsew')

        gap_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.gap_v_right_var,
            width=25
        )
        gap_v_right_input.grid(column=3, row=4, sticky='nsew')

        power_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.power_overall_var,
            width=25
        )
        power_overall_input.grid(column=1, row=5, sticky='nsew')

        power_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.power_v_left_var,
            width=25
        )
        power_v_left_input.grid(column=2, row=5, sticky='nsew')

        power_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.power_v_right_var,
            width=25
        )
        power_v_right_input.grid(column=3, row=5, sticky='nsew')

        eye_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.eye_overall_var,
            width=25
        )
        eye_overall_input.grid(column=1, row=6, sticky='nsew')

        eye_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.eye_v_left_var,
            width=25
        )
        eye_v_left_input.grid(column=2, row=6, sticky='nsew')

        eye_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.eye_v_right_var,
            width=25
        )
        eye_v_right_input.grid(column=3, row=6, sticky='nsew')

    def get_batting_weights(self):
        """Get the weights from the inputs."""
        weights = {}

        def parse(var):
            try:
                return float(var.get())
            except ValueError:
                return 1

        weights['BABIP'] = parse(self.babip_overall_var)
        weights['BABIP vL'] = parse(self.babip_v_left_var)
        weights['BABIP vR'] = parse(self.babip_v_right_var)
        weights['Avoid Ks'] = parse(self.avoid_k_overall_var)
        weights['Avoid K vL'] = parse(self.avoid_k_left_var)
        weights['Avoid K vR'] = parse(self.avoid_k_right_var)
        weights['Gap'] = parse(self.gap_overall_var)
        weights['Gap vL'] = parse(self.gap_v_left_var)
        weights['Gap vR'] = parse(self.gap_v_right_var)
        weights['Power'] = parse(self.power_overall_var)
        weights['Power vL'] = parse(self.power_v_left_var)
        weights['Power vR'] = parse(self.power_v_right_var)
        weights['Eye'] = parse(self.eye_overall_var)
        weights['Eye vL'] = parse(self.eye_v_left_var)
        weights['Eye vR'] = parse(self.eye_v_right_var)

        return weights
