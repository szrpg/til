from curses.ascii import US
from re import U


class TesstSignupAPIView:
    @pytest.fixture
    def target_api(self):
        return '/api/signup'

    def test_do_signup(self, target_api, django_app):
        # 準備
        from account.models import User
        params = {
            'email': 'xxx',
            'name': 'xxx',
            'password': 'xxxxxxx'
        }

        # 実行
        res = django_app.post_json(target_api, params=params)

        # 検証
        user = User.objecs.all()[0]
        expected = {
            'status_code': 201,
            'user_email': 'xxx'
        }
        actual = {
            'status_code': res.status_code,
            'user_email': user.email
        }
        assert expected == actual