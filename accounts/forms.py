from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

# dev_10
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "job",
            "gender",
        ]

#  dev_11
    def init(self, args, **kwargs):
        super().init(args, **kwargs)

        # 모든 필드에 Bootstrap form-control 클래스 추가
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )

        # 성별 선택을 위한 Bootstrap form-select 클래스 추가
        self.fields["gender"].widget.attrs.update({"class": "form-select"})

        # 직업 선택을 위한 Bootstrap form-select 클래스 추가
        self.fields["job"].widget.attrs.update({"class": "form-select"})