#pragma once
#include "TrenchCoat.h"
#include "TrenchCoatRepo.h"

class UndoAction {
public:
	virtual void executeUndo() = 0;
	virtual ~UndoAction() {};
};

class UndoAdd : public UndoAction {
private:
	 TrenchCoat trench;
	TrenchCoatRepo* repo;
public:
	UndoAdd(TrenchCoatRepo* trenchRepo, const TrenchCoat& trenchCoat) : repo(trenchRepo),trench(trenchCoat) {}
	void executeUndo() override {
		repo->deleteTrench(trench.getName());
	}
};

class UndoRemove : public UndoAction {
private:
	 TrenchCoat trench;
	TrenchCoatRepo* repo;
public:
	UndoRemove(TrenchCoatRepo* trenchRepo, const TrenchCoat& trenchCoat) : repo(trenchRepo),trench(trenchCoat) {}
	void executeUndo() override {
		repo->addTrench(trench.getPrice(), trench.getName(), trench.getPhoto(), trench.getSize());
	}
};

class UndoUpdate : public UndoAction {
private:
	 TrenchCoat trench;
	TrenchCoatRepo* repo;
public:
	UndoUpdate(TrenchCoatRepo* trenchRepo, const TrenchCoat& trenchCoat) : repo(trenchRepo),trench(trenchCoat) {}

	void executeUndo() override {
		repo->updateTrench(trench.getPrice(), trench.getName(), trench.getPhoto(), trench.getSize());
	}
};

class RedoAction {
public:
	virtual void executeRedo() = 0;
	virtual ~RedoAction() {};
};

class RedoAdd : public RedoAction {
private:
	 TrenchCoat trench;
	TrenchCoatRepo* repo;
public:
	RedoAdd(TrenchCoatRepo* trenchRepo, const TrenchCoat& trenchCoat) : repo(trenchRepo),trench(trenchCoat) {}

	void executeRedo() override {
		repo->addTrench(trench.getPrice(), trench.getName(), trench.getPhoto(), trench.getSize());
		//repo->deleteTrench(trench.getName());
	}
};

class RedoRemove : public RedoAction {
private:
	 TrenchCoat trench;
	TrenchCoatRepo* repo;
public:
	RedoRemove(TrenchCoatRepo* trenchRepo, const TrenchCoat& trenchCoat) : repo(trenchRepo),trench(trenchCoat) {}

	void executeRedo() override {
		repo->deleteTrench(trench.getName());
		//repo->addTrench(trench.getPrice(), trench.getName(), trench.getPhoto(), trench.getSize());
	}
};

class RedoUpdate : public RedoAction {
private:
	 TrenchCoat trench;
	TrenchCoatRepo* repo;
public:
	RedoUpdate(TrenchCoatRepo* trenchRepo, const TrenchCoat& trenchCoat) : repo(trenchRepo),trench(trenchCoat) {}

	void executeRedo() override {
		repo->updateTrench(trench.getPrice(), trench.getName(), trench.getPhoto(), trench.getSize());
	}
};