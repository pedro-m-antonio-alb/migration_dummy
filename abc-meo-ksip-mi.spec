%define disttype %{expand:%%(/usr/lib/rpm/redhat/dist.sh --disttype)}
%define distnum %{expand:%%(/usr/lib/rpm/redhat/dist.sh --distnum)}
%{!?rpm_name:    %global rpm_name    %(cat .build.n) }
%{!?rpm_version: %global rpm_version %(cat .build.v) }
%{!?rpm_release: %global rpm_release 1 }

%define _prefix /opt/ptin/abc-meo-ksip
%define _user ksipims
%define _group ptin

%define schema_ksipims abcmeo

%if %{distnum} == 6
%define dbtype_pg pgsql95
%endif
%if %{distnum} == 7
%define dbtype_pg pgsql12
%endif

Name: %{rpm_name}
Version: %{rpm_version}
Release: %{rpm_release}.%{disttype}%{distnum}
Summary: migracoes SQL da solução abc-meo-ksip
License: Altice Labs License Terms and Conditions (see http://www.alticelabs.com/licenses/)
Packager: ABCMEOKSIP
Group: ptin/sol-misc
Source: %{name}-%{version}.tar.gz
BuildRequires:  redhat-rpm-config
%if %{distnum} == 6
Requires: pdsngtools-migrate-libpgsql95 >= 3.0.0, pdsngtools-migrate-libpgsql95 < 6.2.0
%endif
%if %{distnum} == 7
Requires: pdsngtools-migrate-libpgsql12 >= 6.1.1, pdsngtools-migrate-libpgsql12 < 6.2.0
%endif

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
This system provides the following packages:
* abc-meo-ksip-mi, abc-meo-ksip SQL migrations


%package        %{dbtype_pg} 
Summary:        %{name} db migration for Postgres %{dbtype_pg}
Group:          ptin/prod
BuildArch:      noarch
BuildRequires:  redhat-rpm-config
Provides: %{name} = %(cat .build.v)-%{rpm_release}
%if %{distnum} == 6
Requires:       pdsngtools-migrate >= 1
Requires:       pdsngtools-migrate-libpgsql95 >= 3.0.0, pdsngtools-migrate-libpgsql95 < 6.2.0
%endif
%if %{distnum} == 7
Requires:       pdsngtools-migrate >= 1
Requires:       pdsngtools-migrate-libpgsql12 >= 6.1.1, pdsngtools-migrate-libpgsql12 < 6.2.0
%endif

%if %{distnum} == 6
%description pgsql95
%endif
%if %{distnum} == 7
%description pgsql12
%endif

%{name} kamailio-ksipims DB migration for Postgres %{dbtype_pg}

%prep
%setup

%build
%configure
make

%install
rm -rf %{buildroot}

##############
#   ABCPROD
##############
mkdir -p %{buildroot}/%{_prefix}/ABCPROD/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/ABCPROD/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/ABCPROD/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/ABCPROD/model/scripts/*.sql %{buildroot}/%{_prefix}/ABCPROD/db/%{dbtype_pg}/steps/model/scripts/


##############
#   DEV
##############
mkdir -p %{buildroot}/%{_prefix}/DEV/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/DEV/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/DEV/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/DEV/model/scripts/*.sql %{buildroot}/%{_prefix}/DEV/db/%{dbtype_pg}/steps/model/scripts/


##############
#   IST1
##############
mkdir -p %{buildroot}/%{_prefix}/IST1/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/IST1/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/IST1/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/IST1/model/scripts/*.sql %{buildroot}/%{_prefix}/IST1/db/%{dbtype_pg}/steps/model/scripts/


##############
#   IST2
##############
mkdir -p %{buildroot}/%{_prefix}/IST2/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/IST2/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/IST2/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/IST2/model/scripts/*.sql %{buildroot}/%{_prefix}/IST2/db/%{dbtype_pg}/steps/model/scripts/


##############
#   IST3
##############
mkdir -p %{buildroot}/%{_prefix}/IST3/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/IST3/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/IST3/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/IST3/model/scripts/*.sql %{buildroot}/%{_prefix}/IST3/db/%{dbtype_pg}/steps/model/scripts/


##############
#   IST4
##############
mkdir -p %{buildroot}/%{_prefix}/IST4/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/IST4/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/IST4/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/IST4/model/scripts/*.sql %{buildroot}/%{_prefix}/IST4/db/%{dbtype_pg}/steps/model/scripts/


##############
#    PROD 
##############
mkdir -p %{buildroot}/%{_prefix}/PROD/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/PROD/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/PROD/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/PROD/model/scripts/*.sql %{buildroot}/%{_prefix}/PROD/db/%{dbtype_pg}/steps/model/scripts/


##############
#  QA
##############
mkdir -p %{buildroot}/%{_prefix}/QA/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/QA/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/QA/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/QA/model/scripts/*.sql %{buildroot}/%{_prefix}/QA/db/%{dbtype_pg}/steps/model/scripts/


##############
#  TCD
##############
mkdir -p %{buildroot}/%{_prefix}/TCD/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/TCD/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/TCD/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/TCD/model/scripts/*.sql %{buildroot}/%{_prefix}/TCD/db/%{dbtype_pg}/steps/model/scripts/


##############
#   UAT
##############
mkdir -p %{buildroot}/%{_prefix}/UAT/db/%{dbtype_pg}/steps/model/scripts
mkdir -p %{buildroot}/%{_prefix}/UAT/db/%{dbtype_pg}/mi
install -p -m 755 %{_builddir}/%{name}-%{version}/mi/* %{buildroot}/%{_prefix}/UAT/db/%{dbtype_pg}/mi/
install -p -m 755 %{_builddir}/%{name}-%{version}/pgsql/UAT/model/scripts/*.sql %{buildroot}/%{_prefix}/UAT/db/%{dbtype_pg}/steps/model/scripts/


%clean
rm -rf %{buildroot}

################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-ABCPROD
Summary:    Production rules

%description db-data-%{dbtype_pg}-ABCPROD
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-ABCPROD


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-ABCPROD

%preun db-data-%{dbtype_pg}-ABCPROD

%postun db-data-%{dbtype_pg}-ABCPROD

%files db-data-%{dbtype_pg}-ABCPROD
#%defattr(-,%{_user},%{_group})
#%dir %{_prefix}/%{dbtype_pg}/steps/ABCPROD
#%dir %{_prefix}/%{dbtype_pg}/steps/ABCPROD/model
#%dir %{_prefix}/%{dbtype_pg}/steps/ABCPROD/model/scripts
#%{_prefix}/%{dbtype_pg}/steps/*.sql
#%{_prefix}/%{dbtype_pg}/steps/ABCPROD/model/scritps/*.sql
#%{_prefix}/%{dbtype_pg}/mi
%dir %{_prefix}/ABCPROD
%dir %{_prefix}/ABCPROD/db
%dir %{_prefix}/ABCPROD/db/%{dbtype_pg}
%dir %{_prefix}/ABCPROD/db/%{dbtype_pg}/steps
%{_prefix}/ABCPROD/db/%{dbtype_pg}/steps/*
%{_prefix}/ABCPROD/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-DEV
Summary:    Production rules

%description db-data-%{dbtype_pg}-DEV
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-DEV


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-DEV

%preun db-data-%{dbtype_pg}-DEV

%postun db-data-%{dbtype_pg}-DEV

%files db-data-%{dbtype_pg}-DEV
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/DEV
%dir %{_prefix}/DEV/db
%dir %{_prefix}/DEV/db/%{dbtype_pg}
%dir %{_prefix}/DEV/db/%{dbtype_pg}/steps
%{_prefix}/DEV/db/%{dbtype_pg}/steps/*
%{_prefix}/DEV/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-IST1
Summary:    Production rules

%description db-data-%{dbtype_pg}-IST1
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-IST1


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-IST1

%preun db-data-%{dbtype_pg}-IST1

%postun db-data-%{dbtype_pg}-IST1

%files db-data-%{dbtype_pg}-IST1
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/IST1
%dir %{_prefix}/IST1/db
%dir %{_prefix}/IST1/db/%{dbtype_pg}
%dir %{_prefix}/IST1/db/%{dbtype_pg}/steps
%{_prefix}/IST1/db/%{dbtype_pg}/steps/*
%{_prefix}/IST1/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-IST2
Summary:    Production rules

%description db-data-%{dbtype_pg}-IST2
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-IST2


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-IST2

%preun db-data-%{dbtype_pg}-IST2

%postun db-data-%{dbtype_pg}-IST2

%files db-data-%{dbtype_pg}-IST2
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/IST2
%dir %{_prefix}/IST2/db
%dir %{_prefix}/IST2/db/%{dbtype_pg}
%dir %{_prefix}/IST2/db/%{dbtype_pg}/steps
%{_prefix}/IST2/db/%{dbtype_pg}/steps/*
%{_prefix}/IST2/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-IST3
Summary:    Production rules

%description db-data-%{dbtype_pg}-IST3
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-IST3


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-IST3

%preun db-data-%{dbtype_pg}-IST3

%postun db-data-%{dbtype_pg}-IST3

%files db-data-%{dbtype_pg}-IST3
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/IST3
%dir %{_prefix}/IST3/db
%dir %{_prefix}/IST3/db/%{dbtype_pg}
%dir %{_prefix}/IST3/db/%{dbtype_pg}/steps
%{_prefix}/IST3/db/%{dbtype_pg}/steps/*
%{_prefix}/IST3/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-IST4
Summary:    Production rules

%description db-data-%{dbtype_pg}-IST4
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-IST4


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-IST4

%preun db-data-%{dbtype_pg}-IST4

%postun db-data-%{dbtype_pg}-IST4

%files db-data-%{dbtype_pg}-IST4
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/IST4
%dir %{_prefix}/IST4/db
%dir %{_prefix}/IST4/db/%{dbtype_pg}
%dir %{_prefix}/IST4/db/%{dbtype_pg}/steps
%{_prefix}/IST4/db/%{dbtype_pg}/steps/*
%{_prefix}/IST4/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-PROD
Summary:    Production rules

%description db-data-%{dbtype_pg}-PROD
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-PROD


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-PROD

%preun db-data-%{dbtype_pg}-PROD

%postun db-data-%{dbtype_pg}-PROD

%files db-data-%{dbtype_pg}-PROD
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/PROD
%dir %{_prefix}/PROD/db
%dir %{_prefix}/PROD/db/%{dbtype_pg}
%dir %{_prefix}/PROD/db/%{dbtype_pg}/steps
%{_prefix}/PROD/db/%{dbtype_pg}/steps/*
%{_prefix}/PROD/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-QA
Summary:    Production rules

%description db-data-%{dbtype_pg}-QA
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-QA


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-QA

%preun db-data-%{dbtype_pg}-QA

%postun db-data-%{dbtype_pg}-QA

%files db-data-%{dbtype_pg}-QA
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/QA
%dir %{_prefix}/QA/db
%dir %{_prefix}/QA/db/%{dbtype_pg}
%dir %{_prefix}/QA/db/%{dbtype_pg}/steps
%{_prefix}/QA/db/%{dbtype_pg}/steps/*
%{_prefix}/QA/db/%{dbtype_pg}/mi


################################################################################################
#                ABC-MEO-KSIP-MI RPM SECTION                                                   #
%package    db-data-%{dbtype_pg}-TCD
Summary:    Production rules

%description db-data-%{dbtype_pg}-TCD
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-TCD


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-TCD

%preun db-data-%{dbtype_pg}-TCD

%postun db-data-%{dbtype_pg}-TCD

%files db-data-%{dbtype_pg}-TCD
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/TCD
%dir %{_prefix}/TCD/db
%dir %{_prefix}/TCD/db/%{dbtype_pg}
%dir %{_prefix}/TCD/db/%{dbtype_pg}/steps
%{_prefix}/TCD/db/%{dbtype_pg}/steps/*
%{_prefix}/TCD/db/%{dbtype_pg}/mi


################################################################################################
#                 ABC-MEO-KSIP-MI RPM SECTION                                                  #
%package    db-data-%{dbtype_pg}-UAT
Summary:    Production rules

%description db-data-%{dbtype_pg}-UAT
Production Rules.
################################  PRE/POST RPM DB CLI  #########################################
%pre db-data-%{dbtype_pg}-UAT


if [ $1 -eq 1 ]; then

     # if not exist add group
     if ! /usr/bin/getent group %{_group} &>/dev/null; then
           /usr/sbin/groupadd -r %{_group} &>/dev/null
     fi


     # if not exist add the omuser user        
     if ! /usr/bin/id %{_user} &>/dev/null; then
           /usr/sbin/useradd -s /bin/bash -d %{_prefix} -c "%{_user} user" -g %{_group} %{_user} -p %{_user} &>/dev/null
           echo %{_user} | passwd --stdin %{_user} &>/dev/null
     fi

fi

%post db-data-%{dbtype_pg}-UAT

%preun db-data-%{dbtype_pg}-UAT

%postun db-data-%{dbtype_pg}-UAT

%files db-data-%{dbtype_pg}-UAT
%defattr(-,%{_user},%{_group})
%dir %{_prefix}/UAT
%dir %{_prefix}/UAT/db
%dir %{_prefix}/UAT/db/%{dbtype_pg}
%dir %{_prefix}/UAT/db/%{dbtype_pg}/steps
%{_prefix}/UAT/db/%{dbtype_pg}/steps/*
%{_prefix}/UAT/db/%{dbtype_pg}/mi



%changelog
* Thu Feb 3 2022 Virgilio Cunha <virgilio-a-cunha@alticelabs.com> 1
- First version
