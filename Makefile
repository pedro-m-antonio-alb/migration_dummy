MYHOME=$(shell pwd)
NAME=$(shell cat .build.n)
#VERSION=$(shell cat .build.v)
VERSION=$(shell if [ `cat .build.t` == "beta" ]; then echo beta; else echo `cat .build.v`; fi)
 

_NAME=$(shell echo $$NAME|awk -F "-mi$$" '{print $$1}')
prefix = /opt/ptin/$(_NAME)
buildroot =/tmp
#dbtype=pgsql95
 

all: clean build

 

clean:
	rm -rf tmp/$(NAME)-$(VERSION);\
	rm -f $(NAME)-$(VERSION).tar.gz

dist:
	mkdir -p tmp/$(NAME)-$(VERSION);\
	cp -rf `ls -1 -A --ignore=rpmbuild --ignore=tmp --ignore=*.tar.gz --ignore=.svn --ignore=.*.swp` tmp/$(NAME)-$(VERSION)/;\
	cd tmp/;\
	tar czvf $(NAME)-$(VERSION).tar.gz --exclude='.svn' $(NAME)-$(VERSION);\
	mv $(NAME)-$(VERSION).tar.gz $(MYHOME)

build:
 

install:
	
	@echo "buildroot=$(buildroot)"
	@echo "prefix=$(prefix)"
	mkdir -p $(buildroot)$(prefix)
	#mkdir -p $(buildroot)$(prefix)/db/pgsql/steps/model/tab/
	#mkdir -p $(buildroot)$(prefix)/db/pgsql/mi
	#make-install-dir -f -w . $(dbtype) $(buildroot)$(prefix)
test:
	echo "Devem-se colocar a execucao dos testes unitarios"
