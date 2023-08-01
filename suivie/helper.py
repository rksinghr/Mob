toolbar1 = """
MDScreen:

    MDBottomNavigation:
        selected_color_background: "red"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'

            MDLabel:
                text: 'This is home'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Pulse'
            icon: 'heart'

            MDLabel:
                text: 'Record Resting heart rate'
                halign: 'center'
                pos_hint: {"center_x": 0.5, "center_y": 0.7}

            MDTextField:
                id: heart_rate
                hint_text: "Heart rate"
                icon_right: "heart"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.6}

            MDRoundFlatButton:
                text: "Submit"
                font_size: 12
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_press: app.logger()

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Record'
            icon: 'clock'

            MDLabel:
                id: tt_lable
                text: "Trak My Time"
                font_size: 20
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                padding_y: 5
                pos_hint: {"center_x": 0.5, "center_y": 0.9}

            MDTextField:
                id: tt_date
                hint_text: "Enter Date"
                icon_right: "clock"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.8}

            MDTextField:
                id: tt_event
                hint_text: "Enter Event"
                icon_right: "bicycle"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.7}

            MDTextField:
                id: tt_Fteeth
                hint_text: "Front Gear teeth"
                icon_right: "cog"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
            
            MDTextField:
                id: tt_Rteeth
                hint_text: "Rear Gear teeth"
                icon_right: "cog"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDTextField:
                id: lap1
                hint_text: "Lap 1"
                icon_right: "clock"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.4}

            MDTextField:
                id: lap2
                hint_text: "Lap 2"
                icon_right: "clock"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.3}

            MDTextField:
                id: lap3
                hint_text: "Lap 3"
                icon_right: "clock"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.2}

            MDRoundFlatButton:
                text: "Submit"
                font_size: 12
                pos_hint: {"center_x": 0.5, "center_y": 0.1}
                on_press: app.logger()
        
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Login'
            icon: 'account'
            
            MDLabel:
                id: welcome_label
                text: "WELCOME"
                font_size: 40
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                padding_y: 15
                pos_hint: {"center_x": 0.5, "center_y": 0.8}

            MDTextField:
                id: user
                hint_text: "username"
                icon_right: "account"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.6}

            MDTextField:
                id: password
                hint_text: "password"
                icon_right: "eye-off"
                size_hint_x: None
                width: 200
                font_size: 18
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                password: True

            MDRoundFlatButton:
                text: "LOG IN"
                font_size: 12
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                on_press: app.logger()

            MDRoundFlatButton:
                text: "CLEAR"
                font_size: 12
                pos_hint: {"center_x": 0.5, "center_y": 0.2}
                on_press: app.clear()
"""