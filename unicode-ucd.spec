Summary:	Unicode Character Database
Name:		unicode-ucd
Version:	6.2.0
Release:	1
License:	MIT
URL:		http://www.unicode.org/ucd/
Group:		Libraries
Source0:	http://www.unicode.org/Public/zipped/%{version}/UCD.zip
# Source0-md5:	cbdd64a505106fcc3ae8692e42d57f42
# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source1:	http://www.unicode.org/copyright.html
# Source1-md5:	25bbbabca50c813a01c99db97286d110
BuildRequires:	unzip
BuildArch:	noarch

%description
The Unicode Character Database (UCD) consists of a number of data
files listing Unicode character properties and related data. It also
includes data files containing test data for conformance to several
important Unicode algorithms.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/unicode/ucd
cp -a . $RPM_BUILD_ROOT%{_datadir}/unicode/ucd
cp -p %{SOURCE1} .

%files
%defattr(644,root,root,755)
%doc copyright.html
%dir %{_datadir}/unicode
%{_datadir}/unicode/ucd

%clean
rm -rf $RPM_BUILD_ROOT
