from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(required=False)
    hp = forms.IntegerField(required=False)
    hp_min = forms.IntegerField(required=False)
    hp_max = forms.IntegerField(required=False)
    defense = forms.IntegerField(required=False)
    defense_min = forms.IntegerField(required=False)
    defense_max = forms.IntegerField(required=False)
    page = forms.IntegerField(required=False)
    name_distance = forms.IntegerField(required=False)

    def range_filters(self):
        filter_condition = dict()
        for k, v in self.cleaned_data.items():
            if not v:
                continue

            if '_' in k:
                param, condition = k.split('_', 1)
                if condition == 'max':
                    filter_condition[f'{param}__lte'] = v
                elif condition == 'min':
                    filter_condition[f'{param}__gte'] = v
        return filter_condition
