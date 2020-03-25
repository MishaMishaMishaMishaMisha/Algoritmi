#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

void quickSort(int *numbers, int left, int right)
{
    int pivot;
    int l = left;
    int r = right;
    pivot = numbers[left];
    while (left < right)
    {
        while ((numbers[right] >= pivot) && (left < right))
        {
            right--;
        }
        if (left != right)
        {
            numbers[left] = numbers[right];
            left++;
        }
        while ((numbers[left] <= pivot) && (left < right))
        {
            left++;
        }
        if (left != right)
        {
            numbers[right] = numbers[left];
            right--;
        }
    }
    numbers[left] = pivot;
    pivot = left;
    left = l;
    right = r;
    if (left < pivot)
    {
        quickSort(numbers, left, pivot - 1);
    }
    if (right > pivot)
    {
        quickSort(numbers, pivot + 1, right);
    }
}

int main()
{
    string N, ss, s;
    int *ar;

    getline(cin, N);
    int n = atoi(N.c_str());
    ar = new int[n];

    getline(cin, ss);
    s = ss + " 0";

    string::size_type sz = 0;
    int index = 0;
    while(sz < s.length())
    {
        int i_dec = stoi(s, &sz);
        ar[index] = i_dec;
        s = s.substr(sz + 1);
        index++;
    }

    quickSort(ar, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << ar[i] << " ";
    }
}
