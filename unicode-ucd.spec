Summary:	Unicode Character Database
Summary(pl.UTF-8):	Unicode Character Database - baza danych znaków Unicode
Name:		unicode-ucd
Version:	12.1.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.unicode.org/Public/zipped/%{version}/UCD.zip
# Source0-md5:	430cbdac2615451571dd69a976dd08f6
Source1:	http://www.unicode.org/Public/zipped/%{version}/Unihan.zip
# Source1-md5:	55a93848bb2810b942d607e55ad01bf3
# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source2:	http://www.unicode.org/copyright.html
# Source2-md5:	01c7e36383a1654909592aa0f9ba977e
URL:		http://www.unicode.org/ucd/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Unicode Character Database (UCD) consists of a number of data
files listing Unicode character properties and related data. It also
includes data files containing test data for conformance to several
important Unicode algorithms.

%description -l pl.UTF-8
Unicode Character Database (UCD) to baza danych znaków Unicode,
składająca się z kilku plików z danymi, opisujących właściwości znaków
Unicode i powiązane dane. Zawiera także pliki z danymi zawierające
dane do testów zgodności z kilkoma ważnymi algorytmami Unicode.

%package testdata
Summary:	Unicode Character Database - conformance test data
Summary(pl.UTF-8):	Unicode Character Database - dane do testów zgodności
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description testdata
This package contains data files containing test data for conformance
to several important Unicode algorithms.

%description testdata -l pl.UTF-8
Ten pakiet zawiera pliki z danymi zawierające dane do testów zgodności
z kilkoma ważnymi algorytmami Unicode.

%package charts
Summary:	Ideograph charts from Unicode Character Database
Summary(pl.UTF-8):	Zestawienie ideogramów z bazy danych znaków Unicode
Group:		Documentation

%description charts
Ideograph charts from Unicode Character Database.

%description charts -l pl.UTF-8
Zestawienie ideogramów z bazy danych znaków Unicode.

%package unihan
Summary:	Unicode Han Database
Summary(pl.UTF-8):	Baza danych Unicode Han
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description unihan
This package contains archive of data files for the Unified Han
database of Hanzi/Kanji/Hanja Chinese characters.

%description unihan -l pl.UTF-8
Ten pakiet zawiera archiwum plików bazy danych Unified Han, obejmującą
chińskie znaki Hanzi/Kanji/Hanja.

%prep
%setup -q -c

cp -p %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/unicode/ucd

cp -pr *.txt auxiliary extracted $RPM_BUILD_ROOT%{_datadir}/unicode/ucd
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/unicode/ucd

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/unicode/ucd/ReadMe.txt
%{__rm} $RPM_BUILD_ROOT%{_datadir}/unicode/ucd/auxiliary/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NamesList.html ReadMe.txt copyright.html
%dir %{_datadir}/unicode
%dir %{_datadir}/unicode/ucd
%{_datadir}/unicode/ucd/ArabicShaping.txt
%{_datadir}/unicode/ucd/BidiBrackets.txt
%{_datadir}/unicode/ucd/BidiMirroring.txt
%{_datadir}/unicode/ucd/Blocks.txt
%{_datadir}/unicode/ucd/CJKRadicals.txt
%{_datadir}/unicode/ucd/CaseFolding.txt
%{_datadir}/unicode/ucd/CompositionExclusions.txt
%{_datadir}/unicode/ucd/DerivedAge.txt
%{_datadir}/unicode/ucd/DerivedCoreProperties.txt
%{_datadir}/unicode/ucd/DerivedNormalizationProps.txt
%{_datadir}/unicode/ucd/EastAsianWidth.txt
%{_datadir}/unicode/ucd/EmojiSources.txt
%{_datadir}/unicode/ucd/EquivalentUnifiedIdeograph.txt
%{_datadir}/unicode/ucd/HangulSyllableType.txt
%{_datadir}/unicode/ucd/Index.txt
%{_datadir}/unicode/ucd/IndicPositionalCategory.txt
%{_datadir}/unicode/ucd/IndicSyllabicCategory.txt
%{_datadir}/unicode/ucd/Jamo.txt
%{_datadir}/unicode/ucd/LineBreak.txt
%{_datadir}/unicode/ucd/NameAliases.txt
%{_datadir}/unicode/ucd/NamedSequences.txt
%{_datadir}/unicode/ucd/NamedSequencesProv.txt
%{_datadir}/unicode/ucd/NamesList.txt
%{_datadir}/unicode/ucd/NormalizationCorrections.txt
%{_datadir}/unicode/ucd/NushuSources.txt
%{_datadir}/unicode/ucd/PropList.txt
%{_datadir}/unicode/ucd/PropertyAliases.txt
%{_datadir}/unicode/ucd/PropertyValueAliases.txt
%{_datadir}/unicode/ucd/ScriptExtensions.txt
%{_datadir}/unicode/ucd/Scripts.txt
%{_datadir}/unicode/ucd/SpecialCasing.txt
%{_datadir}/unicode/ucd/StandardizedVariants.txt
%{_datadir}/unicode/ucd/TangutSources.txt
%{_datadir}/unicode/ucd/USourceData.txt
%{_datadir}/unicode/ucd/UnicodeData.txt
%{_datadir}/unicode/ucd/VerticalOrientation.txt
%dir %{_datadir}/unicode/ucd/auxiliary
%{_datadir}/unicode/ucd/auxiliary/GraphemeBreakProperty.txt
%{_datadir}/unicode/ucd/auxiliary/SentenceBreakProperty.txt
%{_datadir}/unicode/ucd/auxiliary/WordBreakProperty.txt
%{_datadir}/unicode/ucd/extracted

%files testdata
%defattr(644,root,root,755)
%doc auxiliary/{GraphemeBreakTest.html,LineBreakTest.html,SentenceBreakTest.html,WordBreakTest.html}
%{_datadir}/unicode/ucd/BidiCharacterTest.txt
%{_datadir}/unicode/ucd/BidiTest.txt
%{_datadir}/unicode/ucd/NormalizationTest.txt
%{_datadir}/unicode/ucd/auxiliary/GraphemeBreakTest.txt
%{_datadir}/unicode/ucd/auxiliary/LineBreakTest.txt
%{_datadir}/unicode/ucd/auxiliary/SentenceBreakTest.txt
%{_datadir}/unicode/ucd/auxiliary/WordBreakTest.txt

%files charts
%defattr(644,root,root,755)
%doc USourceGlyphs.pdf USourceRSChart.pdf

%files unihan
%defattr(644,root,root,755)
# note: gucharmap expects Unihan.zip as archive, not individual files
%{_datadir}/unicode/ucd/Unihan.zip
