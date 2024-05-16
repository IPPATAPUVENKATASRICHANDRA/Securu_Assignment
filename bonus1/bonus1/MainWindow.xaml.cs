using System.Collections.Generic;
using System.Windows;
using System.Windows.Controls;

namespace bonus
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            List<Item> items = new List<Item>
            {
                new Item("Item 1", "Description 1"),
                new Item("Item 2", "Description 2"),
                new Item("Item 3", "Description 3"),
                new Item("Item 4", "Description 4"),
                new Item("Item 5", "Description 5"),
            };
            itemListView.ItemsSource = items;
        }

        private void itemListView_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if (itemListView.SelectedItem != null)
            {
                Item item = (Item)itemListView.SelectedItem;
                MessageBox.Show(item.Description, item.Name);
            }
        }
    }

    public class Item
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public Item(string name, string description)
        {
            Name = name;
            Description = description;
        }
    }
}
