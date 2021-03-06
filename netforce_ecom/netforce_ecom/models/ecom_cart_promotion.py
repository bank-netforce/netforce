# Copyright (c) 2012-2015 Netforce Co. Ltd.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

from netforce.model import Model, fields
import time


class CartPromotion(Model):
    _name = "ecom.cart.promotion"
    _fields = {
        "cart_id": fields.Many2One("ecom.cart", "Cart", required=True, on_delete="cascade"),
        "promotion_id": fields.Many2One("sale.promotion","Promotion",required=True),
        "product_id": fields.Many2One("product","Discount Product"),
        "qty": fields.Decimal("Discount Qty"),
        "percent": fields.Decimal("Discount Percent"),
        "amount": fields.Decimal("Discount Amount"),
        "cond_product_id": fields.Many2One("product","Condition Product"),
        "cond_qty": fields.Decimal("Condition Qty"),
    }
    _order = "id"

CartPromotion.register()
