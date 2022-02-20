'''コントローラに処理を書かない
'''

@login_required
def item_list_view(request, shop_id):
    shop = get_object_or_404(Shop, shop_id)
    validatte_membership_permission(request.user, shop, Membership.ROLE_OWNER)
    items = Item.objects.filter(shop=shop).published()
    form = ItemSearchForm(request.GET)
    if form.is_valid():
        items = form.filter_items(items)
    return TemplateResponse(
        request,
        'items/item_list.html',
        {'items': items, 'form': form}
    )


'''validatiors.py
'''

from django.core.exceptions import PermissionDenied


def validate_membership_permission(user, shop, role):
    if not user.memberships.filter(role=role, shop=shop).exists():
        raise PermissionDenied


'''forms.py
'''

class ItemSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name',)

    def filter_item(self, items):
        name = self.cleaned_data['name']
        items = items.filter(name__contains=name)
        return items


'''modelss.py
'''

class ItemQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_at__isnull=False)


class Item(models.Modell):
    name = models.CharField(min_length=3, max_length=127)
    published_at = models.DateTimeField(null=True, blank=True)
    objects = ItemQuerySet.as_manager()

    @property
    def price_tax_incl(self):
        return cal_tax_included(self.price)