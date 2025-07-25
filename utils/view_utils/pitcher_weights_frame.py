"""Frame for setting pitcher rating weights."""
import customtkinter as ctk


class PitcherWeightsFrame(ctk.CTkFrame):
    """Custom frame for pitcher weights."""

    def __init__(self, parent):
        """Frame for setting pitcher rating weights."""
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Variables
        self.stuff_oa_var = ctk.StringVar(value='1')
        self.stuff_v_left_var = ctk.StringVar(value='1')
        self.stuff_v_right_var = ctk.StringVar(value='1')
        self.phr_oa_var = ctk.StringVar(value='1')
        self.phr_v_left_var = ctk.StringVar(value='1')
        self.phr_v_right_var = ctk.StringVar(value='1')
        self.pbabip_oa_var = ctk.StringVar(value='1')
        self.pbabip_v_left_var = ctk.StringVar(value='1')
        self.pbabip_v_right_var = ctk.StringVar(value='1')
        self.control_oa_var = ctk.StringVar(value='1')
        self.control_v_left_var = ctk.StringVar(value='1')
        self.control_v_right_var = ctk.StringVar(value='1')

        # Top label
        self.frame_label = ctk.CTkLabel(
            self,
            text='Pitcher Weights',
        )
        self.frame_label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Left side labels
        self.stuff_label = ctk.CTkLabel(
            self,
            text='Stuff'
        )
        self.stuff_label.grid(row=2, column=0, sticky='nsew')

        self.phr_label = ctk.CTkLabel(
            self,
            text='pHR'
        )
        self.phr_label.grid(row=3, column=0, sticky='nsew')

        self.pbabip_label = ctk.CTkLabel(
            self,
            text='pBABIP'
        )
        self.pbabip_label.grid(row=4, column=0, sticky='nsew')

        self.control_label = ctk.CTkLabel(
            self,
            text='Control'
        )
        self.control_label.grid(row=5, column=0, sticky='nsew')

        # Top labels
        self.overall_label = ctk.CTkLabel(
            self,
            text='OA'
        )
        self.overall_label.grid(row=1, column=1, sticky='nsew')

        self.v_left_label = ctk.CTkLabel(
            self,
            text='vL'
        )
        self.v_left_label.grid(row=1, column=2, sticky='nsew')

        self.v_right_label = ctk.CTkLabel(
            self,
            text='vR'
        )
        self.v_right_label.grid(row=1, column=3, sticky='nsew')

        # Input boxes
        self.stuff_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.stuff_oa_var,
            width=25
        )
        self.stuff_overall_input.grid(row=2, column=1, sticky='nsew')

        self.stuff_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.stuff_v_left_var,
            width=25
        )
        self.stuff_v_left_input.grid(row=2, column=2, sticky='nsew')

        self.stuff_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.stuff_v_right_var,
            width=25
        )
        self.stuff_v_right_input.grid(row=2, column=3, sticky='nsew')

        self.phr_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.phr_oa_var,
            width=25
        )
        self.phr_overall_input.grid(row=3, column=1, sticky='nsew')

        self.phr_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.phr_v_left_var,
            width=25
        )
        self.phr_v_left_input.grid(row=3, column=2, sticky='nsew')

        self.phr_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.phr_v_right_var,
            width=25
        )
        self.phr_v_right_input.grid(row=3, column=3, sticky='nsew')

        self.pbabip_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.pbabip_oa_var,
            width=25
        )
        self.pbabip_overall_input.grid(row=4, column=1, sticky='nsew')

        self.pbabip_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.pbabip_v_left_var,
            width=25
        )
        self.pbabip_v_left_input.grid(row=4, column=2, sticky='nsew')

        self.pbabip_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.pbabip_v_right_var,
            width=25
        )
        self.pbabip_v_right_input.grid(row=4, column=3, sticky='nsew')

        self.control_overall_input = ctk.CTkEntry(
            self,
            textvariable=self.control_oa_var,
            width=25
        )
        self.control_overall_input.grid(row=5, column=1, sticky='nsew')

        self.control_v_left_input = ctk.CTkEntry(
            self,
            textvariable=self.control_v_left_var,
            width=25
        )
        self.control_v_left_input.grid(row=5, column=2, sticky='nsew')

        self.control_v_right_input = ctk.CTkEntry(
            self,
            textvariable=self.control_v_right_var,
            width=25
        )
        self.control_v_right_input.grid(row=5, column=3, sticky='nsew')

    def get_pitching_weights(self):
        """Return the selected pitching weights."""
        weights = {}

        def parse(var):
            try:
                return float(var.get())
            except ValueError:
                return 1

        weights['Stuff'] = parse(self.stuff_oa_var)
        weights['Stuff vL'] = parse(self.stuff_v_left_var)
        weights['Stuff vR'] = parse(self.stuff_v_right_var)
        weights['pHR'] = parse(self.phr_oa_var)
        weights['pHR vL'] = parse(self.phr_v_left_var)
        weights['pHR vR'] = parse(self.phr_v_right_var)
        weights['pBABIP'] = parse(self.pbabip_oa_var)
        weights['pBABIP vL'] = parse(self.pbabip_v_left_var)
        weights['pBABIP vR'] = parse(self.pbabip_v_right_var)
        weights['Control'] = parse(self.control_oa_var)
        weights['Control vL'] = parse(self.control_v_left_var)
        weights['Control vR'] = parse(self.control_v_right_var)

        return weights
