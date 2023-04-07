from django import forms
from homepage.models import Blog, Calendar, List, User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'information', 'image']  # 이미지 기능 추가 해야 함
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.FileInput(),
        }
        labels = {
            'title': '제목',
            'information': '내용',
            'image' : '사진',
        }
        
class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['title', 'information', 'start_day', 'finish_day']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'start_day' : forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'finish_day' : forms.DateInput(format=('/%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        labels = {
            'title': '제목',
            'information': '내용',
            'start_day' : '일정 시작 시점',
            'finish_day' : '일정 종료 시점',
        }

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'information', 'due_date', 'money']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'due_date' : forms.DateInput(format=('/%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'money' : forms.NumberInput(attrs={'min': '0', 'class': 'form-control'})
        }
        labels = {
            'title': '제목',
            'information': '내용',
            'due_date' : '회비 납부 종료 시점',
            'money' : '액수',
        }
        
class RegisterForm(forms.ModelForm):
    user_id = forms.CharField(
        label = '아이디',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'user-id',
                'style': 'width:500px; height: 40px; text-align: center; line-height: 30px; margin:0 auto;',
                'placeholder' : '아이디'
                
            }
        ),
        error_messages = { 'required' : '아이디를 입력해주세요.'}
    )
    
    user_pw = forms.CharField(
        label = '비밀번호',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'user-pw',
                'style': 'width:500px; height: 40px; text-align: center; line-height: 30px; margin:0 auto;',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages = { 'required' : '비밀번호를 입력해주세요.'}
    )
    
    user_name = forms.CharField(
        label = '이름',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'user-name',
                'style': 'width:500px; height: 40px; text-align: center; line-height: 30px; margin:0 auto;',
                'placeholder' : '이름'
            }
        ),
        error_messages = { 'required' : '이름을 입력해주세요.'}
    )
    
    user_email = forms.EmailField(
        label = '이메일',
        required = True,
        widget = forms.EmailInput(
            attrs = {
                'class' : 'user-email',
                'style': 'width:500px; height: 40px; text-align: center; line-height: 30px; margin:0 auto;',
                'placeholder' : '이메일'
            }
        ),
        error_messages = { 'required' : '이메일를 입력해주세요.'}
    )
    
    field_order = [
        'user_id',
        'user_pw',
        'user_name',
        'user_email'
    ]

    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pw',
            'user_name',
            'user_email'
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        
        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')
        user_name = cleaned_data.get('user_name', '')
        user_email = cleaned_data.get('user_email', '')
        
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name
        self.user_email = user_email
    
class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length = 32,
        label = '아이디',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'user-id',
                'style': 'width:500px; height: 40px; text-align: center; line-height: 30px; margin:0 auto;',
                'placeholder' : '아이디'
            }
        ),
        error_messages = { 'required' : '아이디를 입력해주세요.'}
    )
        
    user_pw = forms.CharField(
        max_length = 128,
        label = '비밀번호',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'user-pw',
                'style': 'width:500px; height: 40px; text-align: center; line-height: 30px; margin:0 auto;',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages = { 'required' : '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'user_id',
        'user_pw',
    ]
        
    def clean(self):
        cleaned_data = super().clean()
            
        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')

        if user_id == '':
            return self.add_error('user_id', '아이디를 다시 입력해 주세요.')
        elif user_id == '':
            return self.add_error('user_pw', '비밀번호를 다시 입력해 주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id', '아이디가 존재하지 않습니다.')
            try:
                user = User.objects.get(user_pw=user_pw)
            except User.DoesNotExist:
                return self.add_error('user_pw', '비밀번호가 다릅니다.')