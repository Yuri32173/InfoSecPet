from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    FloatField,
    IntegerField,
    PasswordField,
    RadioField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    validators,
)
from wtforms.validators import InputRequired, Length, Optional


class OnboardingDriveUpload(FlaskForm):
    client_id = PasswordField("Client ID", [InputRequired()])
    client_secret = PasswordField("Client secret", [InputRequired()])


class OnboardingBackupForm(FlaskForm):
    source = StringField(
        "Database Source",
        [Length(max=260), InputRequired()],
        render_kw={"value": ".\\client_db.sqlite3", "readonly": True},
    )
    interval = FloatField(
        "Interval",
        [InputRequired()],
        render_kw={
            "placeholder": (
                "Please select the interval type and enter the duration"
            )
        },
    )
    interval_type = RadioField(
        "Interval Type",
        choices=[
            ("min", "Minute"),
            ("hr", "Hour"),
            ("d", "Day"),
            ("wk", "Week"),
            ("mth", "Month"),
        ],
        default="wk",
    )


class BackupFirstForm(FlaskForm):
    source = StringField(
        "Database Source",
        [Length(max=260), InputRequired()],
        render_kw={
            "placeholder": (
                "Please enter file location (including file extension)"
            )
        },
    )
    interval = FloatField(
        "Interval",
        [InputRequired()],
        render_kw={
            "placeholder": (
                "Please select the interval type and enter the duration"
            )
        },
    )
    interval_type = RadioField(
        "Interval Type",
        choices=[
            ("min", "Minute"),
            ("hr", "Hour"),
            ("d", "Day"),
            ("wk", "Week"),
            ("mth", "Month"),
        ],
        default="wk",
    )
    submit = SubmitField("Backup & Save Settings")


from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    SelectMultipleField,
    RadioField,
    DateField,
    IntegerField,
    FloatField,
    validators,
)

class BackupForm(FlaskForm):
    source = StringField(
        "Database Source", [validators.Length(max=260), validators.Optional()],
        render_kw={"placeholder": "Leave empty if no changes"}
    )
    interval = FloatField(
        "Interval", [validators.Optional()],
        render_kw={"placeholder": "Leave empty if no changes"}
    )
    interval_type = RadioField(
        "Interval Type",
        choices=[
            ("min", "Minute"),
            ("hr", "Hour"),
            ("d", "Day"),
            ("wk", "Week"),
            ("mth", "Month"),
        ],
        default="wk"
    )
    manual = SubmitField("Manual Backup")
    update = SubmitField("Backup & Update Settings")

class RequestFilter(FlaskForm):
    query = StringField("Search", [validators.Length(min=1, max=100), validators.Optional()])
    alert_level = SelectField(
        "Alert Level", [validators.InputRequired()],
        choices=[
            ("None", "None"),
            ("High", "High"),
            ("Medium", "Medium"),
            ("Low", "Low"),
        ]
    )
    date = DateField(
        "Date", format="%Y-%m-%d", validators=(validators.Optional(),)
    )
    sort = SelectField(
        "Sort By", choices=[("Latest", "Latest"), ("Oldest", "Oldest")]
    )

class RequestBehaviourForm(FlaskForm):
    url = StringField("URL", [validators.InputRequired(), validators.Length(min=1, max=100)])
    count = IntegerField("URL Accessed Count", [validators.InputRequired()])
    alert_level = SelectField(
        "Alert Level", [validators.InputRequired()],
        choices=[("High", "High"), ("Medium", "Medium"), ("Low", "Low")],
    )
    refresh_time = IntegerField("URL Count refresh time", [validators.InputRequired()])
    refresh_unit = SelectField(
        "Unit Interval", [validators.InputRequired()],
        choices=[
            ("Sec", "Sec"),
            ("Min", "Min"),
            ("Hour", "Hour"),
            ("Day", "Day"),
        ]
    )

class SensitiveFieldForm(FlaskForm):
    sensitive_field = StringField(
        "Sensitive Field", [validators.InputRequired(), validators.Length(min=1, max=100)]
    )
    action = SelectField(
        "Action taken when conditions meet",
        [validators.InputRequired()],
        choices=[
            ("deny_and_alert", "Deny and Alert"),
            ("alert_only", "Alert Only"),
        ]
    )
    occurrence_threshold = IntegerField(
        "Occurrence Threshold", [validators.InputRequired()]
    )
    alert_level = SelectField(
        "Alert Level", [validators.InputRequired()],
        choices=[("High", "High"), ("Medium", "Medium"), ("Low", "Low")],
    )

class WhitelistForm(FlaskForm):
    ip_address = StringField(
        "IP address", [validators.InputRequired(), validators.Length(min=7, max=15)]
    )

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(), validators.Length(max=32)])
    password = PasswordField(
        "Password", [validators.InputRequired(), validators.Length(min=8, max=32)]
    )

class CreateUserForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(), validators.Length(max=32)])
    password = PasswordField(
        "Password", [validators.InputRequired(), validators.Length(min=8, max=32)]
    )
    permissions = SelectMultipleField("Permissions", [validators.InputRequired()])

class CreateAdminUserForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(), validators.Length(max=32)])
    password = PasswordField(
        "Password", [validators.InputRequired(), validators.Length(min=8, max=32)]
    )

class ChoiceForm(FlaskForm):
    model = StringField("Model", validators=[validators.InputRequired()])
    field = StringField("Field", validators=[validators.InputRequired()])
