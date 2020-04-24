//
// Created by Ioana on 17.05.2019.
//

#ifndef MARA_TES_FAKE_REPO_H
#define MARA_TES_FAKE_REPO_H

#include "TrenchCoatRepo.h"
class fake_repo : public TrenchCoatRepo {
public:
	fake_repo();
	~fake_repo();
	void updateTrench(int price, string name, string photo, string size)override;
};


#endif //MARA_TES_FAKE_REPO_H
