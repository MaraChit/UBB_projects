#include "P13.h"
#include "TestP13.h"
#include <assert.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool lessThan(TElem e1, TElem e2) {
	return e1 <= e2;
}

bool greaterThan(TElem e1, TElem e2) {
	return e1 >= e2;
}

vector<TElem> getRandomR1(int from, int to, int middle, int k, int all) {
	vector<TElem> v;
	for (int i = k; i < all; i++) {
		int nr = (rand() % (middle - from)) + from;
		v.push_back(nr);
	}
	for (int i = 0; i < k; i++) {
		int nr = (rand() % (to - middle) + middle+1);
		v.push_back(nr);
	}
	random_shuffle(v.begin(), v.end());
	return v;
}

vector<TElem> getRandomR2(int from, int to, int middle, int k, int all) {
	vector<TElem> v;
	for (int i = 0; i < k; i++) {
		int nr = (rand() % (middle - from)) + from;
		v.push_back(nr);
	}
	for (int i = k; i < all; i++) {
		int nr = (rand() % (to - middle) + middle + 1);
		v.push_back(nr);
	}
	random_shuffle(v.begin(), v.end());
	return v;
}


void checkR1(vector<TElem> l, int from, int to, int middle, int k, int all, vector<TElem> orig) {
	assert(l.size() == max(0, all - k));
	for (vector<TElem>::iterator it = l.begin(); it != l.end(); it++) {
       // cout<<endl<<*it<<" "<<middle;
		assert(*it <= middle);
		vector<TElem>::iterator i = find(orig.begin(), orig.end(), *it);
		assert(i != orig.end());
	}
}

void checkR2(vector<TElem> l, int from, int to, int middle, int k, int all, vector<TElem> orig) {
	assert(l.size() == max(0, all - k));
	for (vector<TElem>::iterator it = l.begin(); it != l.end(); it++) {
		// cout<<endl<<*it<<" "<<middle;
		assert(*it >= middle);
		vector<TElem>::iterator i = find(orig.begin(), orig.end(), *it);
		assert(i != orig.end());
	}
}


void testR1() {

	for (int lower = 10; lower < 1000; lower += 250) {
		for (int upper = 1000; upper < 2000; upper += 300) {
			for (int k = 1; k < 50; k= k + 7) {
				cout << lower << " " << upper << " " << k << endl;
				int middle = (lower + upper) / 2;
				vector<TElem> l = getRandomR1(lower, upper, middle, k, upper - lower + 1);
				vector<TElem> orig = l;
				removeLast(l, lessThan,  k);
				checkR1(l, lower, upper, (lower + upper) / 2, k, upper - lower + 1, orig);

			}
		}
	}
}

void testR2() {
	for (int lower = 10; lower < 1000; lower += 150) {
		for (int upper = 1000; upper < 2000; upper += 250) {
			for (int k = 1; k < 50; k = k + 5) {
				cout << lower << " " << upper << " " << k << endl;
				int middle = (lower + upper) / 2;
				vector<TElem> l = getRandomR2(lower, upper, middle, k, upper - lower + 1);
				vector<TElem> orig = l;
				removeLast(l, greaterThan, k);
				checkR2(l, lower, upper, (lower + upper) / 2, k, upper - lower + 1, orig);

			}
		}
	}
}

vector<TElem> getRandom(int k) {
	vector<TElem> v;
	for (int i = 0; i < k; i++) {
		v.push_back(i);
		v.push_back(-i);
	}
	int n = v.size();
	for (int i = 0; i < n - 1; i++) {
		int j = i + rand() % (n - i);
		swap(v[i], v[j]);
	}
	return v;
}

void verifyGreater(vector<TElem> l, int k) {
	assert(l.size() == k);
	for (vector<TElem>::iterator it = l.begin(); it != l.end(); it++) {
		assert(*it <= k - 1 && *it >= 0);
		//std::cout << *it << std::endl;
	}
}

void verifyLess(vector<TElem> l, int k) {
	assert(l.size() == k);
	for (vector<TElem>::iterator it = l.begin(); it != l.end(); it++) {
		assert(*it >= -k + 1 && *it <= 0);
		//std::cout << *it<<std::endl;
	}
}

void test(Relation r, int k) {
	vector<TElem> l = getRandom(k);
	removeLast(l, r, k);

	if (r == lessThan)
		verifyLess(l, k);
	else
		verifyGreater(l, k);

}

void testP13() {
	for (int k = 5; k < 100; k += 2) {
		test(lessThan, k);
		test(greaterThan, k);
	}
	//std::cout << "Done"<<std::endl;
	vector<TElem> l;
	try {
		removeLast(l, lessThan, 0);
	}
	catch (exception&) {
		assert(true);
	}
	try {
		removeLast(l, greaterThan, -100);
	}
	catch (exception&) {
		assert(true);
	}
	//std::cout << "Done"<<std::endl;
	testR1();
	//std::cout << "Done"<<std::endl;
	testR2();
	//std::cout << "Done" << std::endl;

}
