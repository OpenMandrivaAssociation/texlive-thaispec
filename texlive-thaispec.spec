Name:		texlive-thaispec
Version:	58019
Release:	1
Summary:	Thai Language Typesetting in XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thaispec
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thaispec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thaispec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thaispec.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to input Thai characters directly to
LaTeX documents and choose any (system wide) Thai fonts for
typesetting in XeLaTeX. It also tries to appropriately justify
paragraphs with no more external tools. Required packages are
fontspec, ucharclasses, polyglossia, setspace, kvoptions,
xstring, and xpatch.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/thaispec
%{_texmfdistdir}/tex/latex/thaispec
%doc %{_texmfdistdir}/doc/latex/thaispec

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
