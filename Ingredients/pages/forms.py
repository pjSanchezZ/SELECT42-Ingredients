from django import forms

class select_testform(forms.Form):
  SELVALUE = (
      ('title', 'first'),
      ('content', 'second'),
      ('writer', 'third'),
  )
  sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))
