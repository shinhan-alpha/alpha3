from rest_framework import serializers
from .models import Portfolio, Dividend

class PortfolioSerializer(serializers.ModelSerializer):
    # 로그인 된 정보(CurrentuserDefault)를 자동으로 불러옴
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required=False
    )
    def validate_user(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required')
        return value
    
    class Meta:
        model=Portfolio
        fields='__all__'

class PortfolioDetailSerializer(serializers.ModelSerializer):
    member_acct_no = serializers.SerializerMethodField()
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required=False
    )
    def validate_user(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required')
        return value
    def get_member_acct_no(self, obj):
        return obj.member.acct_no
    
    class Meta:
        model=Portfolio
        fields='__all__'
