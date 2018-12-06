from django.contrib import admin

from django import forms
from django.shortcuts import render, redirect

from .models import System_lens_135, System_lens_medium, Component, Formula

import csv
import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.urls import path, reverse

from import_export.admin import ImportExportModelAdmin



admin.site.register(System_lens_135)
admin.site.register(System_lens_medium)

@admin.register(Component)
class ComponentAdmin(ImportExportModelAdmin):
    pass
#admin.site.register(Component)

@admin.register(Formula)
class FormulaAdmin(ImportExportModelAdmin):
    pass
