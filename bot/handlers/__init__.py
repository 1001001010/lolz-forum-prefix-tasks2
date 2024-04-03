# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from .main_start import dp
from .edit_schedule import dp
from .teachers import dp
from .subjects import dp

__all__ = ['dp']