from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.models import Item, List
from lists.views import home_page
import tvp_traceback


Item.objects.all().delete()
List.objects.all().delete()


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list1 = List()
        list1.save()

        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.list = list1
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = list1
        second_item.save()

        saved_list = List.objects.all()[0]
        self.assertEqual(saved_list, list1)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(
            first_saved_item.text, "The first (ever) list item"
        )
        self.assertEqual(first_saved_item.list, list1)
        self.assertEqual(
            second_saved_item.text, "Item the second"
        )
        self.assertEqual(second_saved_item.list, list1)


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        list1 = List.objects.create()
        response = self.client.get(f"/lists/{list1.id}/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_items(self):
        list1 = List.objects.create()
        Item.objects.create(text="itemey 1", list=list1)
        Item.objects.create(text="itemey 2", list=list1)
        list2 = List.objects.create()
        Item.objects.create(text="itemey 3", list=list2)
        Item.objects.create(text="itemey 4", list=list2)

        response = self.client.get(f"/lists/{list1.id}/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
        self.assertNotContains(response, "itemey 3")
        self.assertNotContains(response, "itemey 4")


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post(
            "/lists/new", data={"item_text": "A new list item"}
        )

        self.assertEqual(List.objects.count(), 1)
        new_item = List.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post(
            "/lists/new", data={"item_text": "A new list item"}
        )
        list1 = List.objects.first()
        self.assertRedirects(response, f"/lists/{list1.id}/")
