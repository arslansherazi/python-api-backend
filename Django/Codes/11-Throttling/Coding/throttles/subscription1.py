from rest_framework.throttling import UserRateThrottle


class BurstRateThrottleSub1(UserRateThrottle):
    scope = 'burst_sub1'


class SustainedRateThrottleSub1(UserRateThrottle):
    scope = 'sustained_sub1'
