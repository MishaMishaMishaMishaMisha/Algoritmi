#include <iostream>
using namespace std;
#include <string>
#include <fstream>
#include <vector>
#include <stdlib.h>

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

void str_to_ar(string s1,int *ar)
{
    string s = s1 + " 0";
    string::size_type sz = 0;
    int index = 0;
    while(sz < s.length())
    {
        int i_dec = stoi(s, &sz);
        ar[index] = i_dec;
        s = s.substr(sz + 1);
        index++;
    }

}

int main()
{
    // 8.4
    int *ar;
    int ab[2];
    ifstream file("input84.txt");
    vector<string> v;
    while (!file.eof())
    {
        string str;
        getline(file, str, '\n');
        v.push_back(str);
    }

    ofstream file1("output84.txt");

    for (int i = 2; i < v.size(); i += 3)
    {
        str_to_ar(v[i], ab);
        int a = ab[0];
        int b = ab[1];
        int siz = atoi((v[i - 2]).c_str());
        ar= new int[siz];
        str_to_ar(v[i - 1], ar);

        quickSort(ar, 0, siz - 1);
        int ii = 0;
        int k = 0;
        while (ii != siz && ar[ii] <= b)
        {
            if (ar[ii] >= a)
            {
                k++;
            }
            ii++;
        }
        file1 << k << "\n";
        delete[] ar;

    }
}
