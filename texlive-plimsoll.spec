Name:		texlive-plimsoll
Version:	56605
Release:	1
Summary:	Fonts with the Plimsoll symbol and LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plimsoll
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plimsoll.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plimsoll.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plimsoll.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides access to the Plimsoll symbol for use
with LaTeX. The Plimsoll symbol is sometimes used in chemistry
for denoting standard states and values. The LaTeX package
provides access to this notation as well. The syntax for
denoting the standard state is the same as suggested in the
Comprehensive LaTeX Symbol List for emulating the Plimsoll
mark.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/plimsoll
%{_texmfdistdir}/tex/latex/plimsoll
%{_texmfdistdir}/fonts/type1/public/plimsoll
%{_texmfdistdir}/fonts/tfm/public/plimsoll
%{_texmfdistdir}/fonts/map/dvips/plimsoll
%{_texmfdistdir}/fonts/enc/dvips/plimsoll
%{_texmfdistdir}/fonts/afm/public/plimsoll
%doc %{_texmfdistdir}/doc/fonts/plimsoll

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
