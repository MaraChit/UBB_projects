//
// Created by Ioana on 17.05.2019.
//

#include "fake_repo.h"
#include "assert.h"
#include "TrenchCoatRepo.h"
fake_repo::fake_repo() {}
fake_repo::~fake_repo() {}

void fake_repo::updateTrench(int price, string name, string photo, string size) {
	if (price != 5)
		throw repository_exception("Not expected value");

	if (name != "BABYTRENCH")
		throw repository_exception("Not expected value");

	if (size != "XS")
		throw repository_exception("Not expected value");
}