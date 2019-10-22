from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


SECURITY_MODES = [
    ('WEP', _('WEP')),
    ('WPA_WPA2P', _('WPA/WPA2 Personal')),
    ('WPA2P', _('WPA2 Personal')),
]


class WifiConfigForm(forms.Form):
    BAD_SSID_CHARS = '+]"\t'
    BAD_FIRST_SSID_CHARS = '!#;'

    ssid = forms.CharField(
        label=_('Station ID'),
        required=True,
    )
    password = forms.CharField(
        label=_('WiFi Password'),
        required=False,
        widget=forms.PasswordInput,
    )
    security_mode = forms.ChoiceField(
        label=_('Security mode'),
        choices=SECURITY_MODES,
    )

    def clean_ssid(self):
        """
        The SSID can consist of up to 32 alphanumeric, case-sensitive,
        characters. The first character cannot be the !, #, or ; character.
        The +, ], /, ", TAB, and trailing spaces are invalid characters
        for SSIDs.

        However, I know for a fact that the "/" is accepted in SSIDs!
        """
        ssid = self.cleaned_data['ssid'].strip()

        if ssid[0] in self.BAD_FIRST_SSID_CHARS:
            raise ValidationError(
                "The SSID should not contain '{}' as the "
                "first symbol.".format(ssid[0]))

        illegal_chars = set(ssid) & set(self.BAD_SSID_CHARS)
        if len(illegal_chars) == 1:
            raise ValidationError(
                "The SSID should not contain the '{}' "
                "symbol.".format(illegal_chars[0]))
        elif len(illegal_chars) > 1:
            illegal_chars_for_display = ", ".join(illegal_chars)
            raise ValidationError(
                "The SSID should not contain any of these symbols: "
                "{}.".format(illegal_chars_for_display))
