from django.utils.functional import cached_property
from rest_framework.exceptions import NotAuthenticated
from rest_framework.generics import get_object_or_404

from apps.core.utils.helpers import nested_getattr
from apps.referrer.models import Referrer


class ReferrerProfileViewSetMixin:
    """
    Defines `referrer` property that returns referrer instance
    passed as `cls.referrer_id_url_kwarg` in url kwargs.

    :cvar referrer_id_url_kwarg: URL kwarg containing referrer id
    """
    referrer_id_url_kwarg = 'referrer_id'

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.referrer

    def get_referrer_queryset(self):
        return Referrer.objects.all()

    @cached_property
    def referrer(self):
        """
        :return: referrer instance for given referrer id
        :raise Http404: If invalid referrer id is passed
        """
        referrer_id = self.kwargs.get(self.referrer_id_url_kwarg)
        if referrer_id == 'me':
            profile = nested_getattr(self, 'request.user.referrer')
            if not profile:
                raise NotAuthenticated
            else:
                return profile
        elif referrer_id is not None:
            return get_object_or_404(
                self.get_referrer_queryset(),
                id=referrer_id
            )
        return None


class CustomerCommonViewSetMixin(ReferrerProfileViewSetMixin):
    """
    Common referrer mixin, which filters queryset by referrer id passed in
    URL kwarg `cls.referrer_id_url_kwarg`.

    Overrides get_queryset to filter queryset according to referrer_id

    It also insert Customer instance as `referrer` in context for serializer.

    :cvar referrer_lookup_field: lookup field used to filter referrer in qs
    """
    referrer_lookup_field = 'referrer'

    def get_queryset(self):
        """
        Filters queryset by referrer id passed in URL kwarg
        `cls.referrer_id_url_kwarg`
        """
        return super().get_queryset().filter(**{
            f"{self.referrer_lookup_field}": self.referrer
        })

    def get_serializer_context(self):
        """
        Updates context to include Customer instance as `referrer`
        """
        ctx = super().get_serializer_context()
        ctx["referrer"] = self.referrer
        return ctx
