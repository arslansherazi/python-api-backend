from rest_framework.throttling import UserRateThrottle


class BurstRateThrottleSub2(UserRateThrottle):
    scope = 'burst_sub2'


class SustainedRateThrottleSub2(UserRateThrottle):
    scope = 'sustained_sub2'
