%global tl_name plimsoll
%global tl_revision 56605
%global tl_version 1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Fonts with the Plimsoll symbol and LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/plimsoll
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plimsoll.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plimsoll.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plimsoll.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides access to the Plimsoll symbol for use with LaTeX.
The Plimsoll symbol is sometimes used in chemistry for denoting standard
states and values. The LaTeX package provides access to this notation as
well. The syntax for denoting the standard state is the same as
suggested in the Comprehensive LaTeX Symbol List for emulating the
Plimsoll mark.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from plimsoll:
Map plimsoll.map
TL_DROPIN_EOF
