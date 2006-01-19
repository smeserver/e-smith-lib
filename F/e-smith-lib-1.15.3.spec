Summary: e-smith server and gateway - library module
%define name e-smith-lib
Name: %{name}
%define version 1.15.3
%define release 34
Version: %{version}
Release: %{release}
License: Artistic
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-lib-1.15.3-02.mitel_patch
Patch1: e-smith-lib-1.15.3-03.mitel_patch
Patch2: e-smith-lib-1.15.3-04.mitel_patch
Patch3: e-smith-lib-1.15.3-05.mitel_patch
Patch4: e-smith-lib-1.15.3-06.mitel_patch
Patch5: e-smith-lib-1.15.3-07.mitel_patch
Patch6: e-smith-lib-1.15.3-08.mitel_patch
Patch7: e-smith-lib-1.15.3-09.mitel_patch
Patch8: e-smith-lib-1.15.3-10.mitel_patch
Patch9: e-smith-lib-1.15.3-11.mitel_patch
Patch10: e-smith-lib-1.15.3-12.mitel_patch
Patch11: e-smith-lib-1.15.3-13.mitel_patch
Patch12: e-smith-lib-1.15.3-14.mitel_patch
Patch13: e-smith-lib-1.15.3-16.mitel_patch
Patch14: e-smith-lib-1.15.3-17.mitel_patch
Patch15: e-smith-lib-1.15.3-18.mitel_patch
Patch16: e-smith-lib-1.15.3-19.mitel_patch
Patch17: e-smith-lib-1.15.3-20.mitel_patch
Patch18: e-smith-lib-1.15.3-21.mitel_patch
Patch19: e-smith-lib-1.15.3-22.mitel_patch
Patch20: e-smith-lib-1.15.3-23.mitel_patch
Patch21: e-smith-lib-1.15.3-24.mitel_patch
Patch22: e-smith-lib-1.15.3-26.mitel_patch
Patch23: e-smith-lib-1.15.3-27.mitel_patch
Patch24: e-smith-lib-1.15.3-RenameDBOnConflict.patch
Patch25: e-smith-lib-1.15.3-NoNewlineCluck.patch
Patch26: e-smith-lib-1.15.3-DotUnderscoreAccounts.patch
Patch27: e-smith-lib-1.15.3-DotUnderscoreAccounts.patch2
Patch28: e-smith-lib-1.15.3-DotUnderscoreAccounts.patch3
Patch29: e-smith-lib-1.15.3-local_access_spec.patch
Patch30: e-smith-lib-1.15.3-no_kudzu.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools >= 1.6.3-01
BuildRequires: e-smith-test >= 0.1.14
Requires: perl, perl(Text::Template)
Requires: perl(Time::HiRes), perl(MIME::Base64)
Requires: perl(Authen::PAM), perl(I18N::AcceptLanguage)
Requires: perl(I18N::LangTags) >= 0.27
Requires: perl(Net::IPv4Addr) >= 0.10

%description
e-smith server and gateway software - library module.

%package Tai64n
Summary: SME Server Tai64n library
Group: Networking/Daemons

%description Tai64n
Split of Tai64n package from main e-smith-lib

%changelog
* Thu Jan 19 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-34
- Remove running of kudzu during NIC probing. TODO: Find a solution
  to system reconfiguration when new hardware is added. [SME: 192]

* Tue Jan 10 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-33
- Fold a.b.c.d/255.255.255.255 to a.b.c.d in local_access_spec() to
  work around bugs in applications which don't accept such specs.
  [SME: 430]

* Mon Jan 9 2006 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-32
- Check whether an accounts db record exists before trying to create
  the dot and underscore pseudonyms (new_record will fail silently)
  and check that the records are pseudonyms before deleting them [SME: 24]

* Mon Jan 9 2006 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-31
- And update POD for last change [SME: 24]

* Mon Jan 9 2006 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-30
- Allow dot and underscore in account names [SME: 24]

* Tue Dec 27 2005 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-29
- Remove newlines from cluck() string and just note that the old
  path was used [SME: 365]

* Sat Dec 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-28
- If db exists in both the old and new locations in 
  initialize_default_databases, rename the one in the new 
  location to db.time(), avoiding the conflict and saving the 
  evidence in case it is needed later [SME: 229]

* Mon Dec 05 2005 Mark Knox <mark_knox@mitel.com>
- [1.15.3-27]
- Moved queueing logic to separate daemon, replaced with FIFO IPC [BZ252

* Thu Dec 01 2005 Mark Knox <mark_knox@mitel.com>
- [1.15.3-26]
- Added event queueing (open source portion) for clustered systems [BZ250]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-25
- Bump release number only

* Thu Nov 24 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.3-24]
- Add missing 'use Locale::gettext' to esmith::console.pm [MN00108804]

* Sun Nov 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-23]
- Clarify logic for stopped services in adjust-services. [SF: 1357629]

* Sun Nov 20 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.3-22]
- Correct adjust-services logic for stopped services [SF: 1357629]

* Wed Nov 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-21]
- Allow services2adjust directories to contain files rather than just dangling
  symlinks. Files can contain more than one actions to perform. [SF: 1270644]

* Wed Nov 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-20]
- Also don't start services if we just want to "once" them. [SF: 1357629]

* Wed Nov 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-19]
- Fix restart of enabled supervised services which we are attempting to stop.
  [SF: 1357629]

* Tue Nov 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-18]
- Set default for $type in esmith::cgi::genSmallCell, to prevent some log
  noise. [SF: 1357830]

* Tue Nov 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-17]
- Pass $EVENT to template expansions in generic_template_expand.
  [SF: MN00106104]

* Tue Nov 15 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.3-16]
- Redirect esmith::config calls on old db paths to the new
  location [SF: 1335865]

* Thu Oct 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-15]
- Fix a few minor spec file portability issues. [SF: 1339729]

* Wed Oct 26 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-14]
- Add it and de to the langtag2locale fixups. [SF: 1338236]

* Tue Oct 11 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-13]
- Build driver list from .ko files as well as .o files. Untaint driver
  names while building list. [SF: 1323270]

* Mon Sep 26 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-12]
- Fix "defaults" handling so that values which evaluate to false are
  not overridden by default. [SF: 1303885]

* Fri Sep 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-11]
- Untaint db names before attempting to move them. [MN00098405]

* Thu Sep 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-10]
- Provide networks method in esmith::NetworksDB. [SF: 1296099]
- Support a "localhost" configuration in esmith::tcpsvd:configure_peers
  [SF: 1294719]

* Tue Sep 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-09]
- Remove deprecated functions from esmith::utils. [SF: 1295851]
- Include only "network" records in local_access_spec. [SF: 1296099]

* Mon Sep 12 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-08]
- Remove warning about explicit path in esmith::db::_db_path.
  [SF: 1286294]

* Fri Sep  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-07]
- Tolerate, but warn about, symlinks in /home/e-smith. [SF: 1216546]

* Fri Sep  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-06]
- Reduce the noise from _file_path() in esmith::DB::db. [SF: 1286294]

* Wed Sep  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-05]
- Fix operation of expandTemplate when taint check is enabled.
  [SF: 1284301]

* Wed Aug 17 2005 Mark Knox <markk@e-smith.com>
- [1.15.3-04]
- Added open_local and open_ro_local methods for clustering [markk MN00094831]

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-03]
- Fix POD error in util.pm.

* Wed Jul 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-02]
- Move databases default location from /home/e-smith to /home/e-smith/db.
  During esmith::utils::initialize_default_databases, move from old to new
  location before doing db migrate actions. [SF: 1216546]

* Wed Jul 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.3-01]
- Roll a new development stream - 1.15.3

* Wed Jul 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.2-04]
- Remove broken MergeDB stuff. [SF: 1246315]

* Wed Jul 27 2005 Mark Knox <markk@e-smith.com>
- [1.15.2-03]
- Fixed misleading comment in util.pm
- Added 'use' statements in Record classes for SOAP compatibility
- Fixed undefined max_len warning
- Added explicit writeconf calls in db::Record.pm, needed for setting props
  via SOAP

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.2-02]
- Allow db open API to use default path if a simple filename
  is provided as arg. This is preparation for move of dbs to
  /home/e-smith/db. Patch by Shad Lords.

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.2-01]
- Roll new development stream - 1.15.2

* Fri Jul 15 2005 Mark Knox <markk@e-smith.com>
- [1.15.1-44]
- Tweak to allow calling _writeconf from SOAP [markk MN00090738]

* Tue Jun 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-43]
- Ensure that esmith::util::LdapPassword returns bare string without
  newline terminator.

* Sun Jun 12 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-42]
- Remove .rpmsave and .rpmnew symlinks (as well as files). [SF: 1217969]
- Handle missing description in pcitables entries.

* Sun Jun 12 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-41]
- Provide feedback (via log messages) from services2adjust. [SF: 1218920]

* Mon May 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-40]
- Add preinstall scripting to create required accounts/groups if they
  don't already exist. [SF: 1210723]

* Thu May  5 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-39]
- Show Text::Template error text rather than inappropriate $! if template
  expansion fails.
- Change error to warning if a config item is set with an empty "type"
  property.

* Thu May  5 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-38]
- Fix esmith::DB::get_prop_and_delete fail if prop is "false" [From Gordon].

* Tue May  3 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-37]
- Update directory list so that ethernet drivers from kernel-unsupported are
  added to "choose by driver" list.

* Sat Mar 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-36]
- Rework esmith::tcpsvd::configure_peers so that it doesn't chdir.
- Fix generic_template_expand so that templates.metadata doesn't
  need to set OUTPUT_FILENAME is TEMPLATE_PATH is changed. This
  matches what expand-template already does.

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-35]
- Change numerous calls to "croak" in esmith::template
  to "carp ...; return", so that problem with any single
  template expansion doesn't terminate calling program.
  [MN00075009]

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-34]
- Add missing "use esmith::util" in esmith::tcpsvd.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-33]
- Add esmith::tcpsvd library for managing tcpsvd "peers"
  directories.

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-32]
- Make template expansion message more succinct.

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-31]
- Remove pseudonyms of pseudonyms when removing user
  accounts. Adapted from patch submitted by Shad. [MN00039941]

* Wed Feb 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-30]
- Fix incompatibility with CentOS's CGI.pm. 

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-29]
- Fix bug in output to empty file when FILTER is used
  during template expansion. [charlieb MN00050075]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-28]
- Refresh contents of /etc/sysconfig/hwconf before listing
  network adaptors [MN00069993]
- Fix typo in documentation of esmith::DB::db - reported from Tanna -
  http://www.livejournal.com/users/gcrumb/61169.html (thanks Dan!)

* Wed Feb 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-27]
- Fix typo. [MN00066059]

* Wed Feb 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-26]
- Use /sbin/e-smith/whiptail if it is available. [MN00066059]

* Mon Feb  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-25]
- Update perms and ownership when expanding templates, regardless of
  whether file content has changed or not. [MN00068043]

* Wed Feb  2 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-24]
- Fix the insertion of implicit actions into sorted action list in
  event.pm. Problem was perl syntax ambiguity.  [MN00066406]

* Fri Jan 28 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-23]
- Really move /home/e-smith/* to e-smith-base. [MN00066635]

* Fri Jan 28 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-22]
- Move /home/e-smith/* to e-smith-base. [MN00066635]
- Move generic-template expand to S05 position in sort, and
  adjust-service to S90. Fix run-time error. [MN00066406]
- Don't attempt to execute non-executable action scripts.

* Thu Jan 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-21]
- Implicitly include template expand and services adjust actions
  in each event if the respective metadata directory exists.
  [MN00066406]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-20]
- Add "adjust" to list of verbs which serviceControl groks,
  to allow for "masq adjust". [MN00065576]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-19]
- Add adjust-services generic action script [MN00065576]

* Tue Jan 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-18]
- Fix typo. [MN00064412]
- Improve die() message in esmith::config::STORE. [MN00064394]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-17]
- Fix broken logging (and reduce logging) in initialize_default_databases.
  [MN00064412]
- Fix inappropriate use of global $_ in initialize_default_databases.
  [MN00064415]

* Thu Dec 23 2004 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-16]
- Read templated file metadata (if any) from file tree under 
  /etc/e-smith/templates.metadata. Update expand-template to
  use current API. [MN00061830]

* Tue Dec 14 2004 Mark Knox <markk@e-smith.com>
- [1.15.1-15]
- Change copyright date to 2004 [markk MN00060958]

* Fri Nov  5 2004 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-14]
- Fix Authen::PAM dependency header [charlieb MN00040240]
- Use kudzu's generated /etc/sysconfig/hwconf file for NIC detection
  [charlieb MN00056220]

* Thu Oct 14 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-13]
- Updated esmith::ethernet's search code to remove File::Find, as it doesn't
  get along with taint checking. [msoulier MN00052510]

* Wed Oct 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-12]
- Updated esmith::ethernet's search code such that is it more adaptable, and
  recurses the directories given. [msoulier MN00052510]

* Wed Oct 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-11]
- Updated esmith::ethernet's search paths for network drivers.
  [msoulier MN00052510]

* Mon Oct  4 2004 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-10]
- Remove dependency on perl(Filter::Handle) [charlieb MN00050075]

* Fri Sep 24 2004 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-09]
- Updated requires with new perl dependencies. [msoulier MN00040240]
- Remove "AutoReqProv: no" so that "Provides" headers are auto-generated.
  [charlieb MN00040240]
- Remove anachronistic "require v5.6.0" directives. [charlieb MN00050370]
- Avoid use of Filter::Handle in esmith::template. [charlieb MN00050075]

* Fri Aug 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-08]
- Added esmith::util::network::isValidEmail function. [msoulier MN00023814]

* Thu Aug 26 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-07]
- Added svdisable to permissible actions in serviceControl.
  [msoulier MN00043056]

* Tue Aug 10 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-06]
- Fixed new methods. Bad else case. [msoulier MN00044891]

* Fri Aug  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-05]
- Added a keys() method. [msoulier MN00041968]

* Fri Aug  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-04]
- Added set_prop and set_value methods in esmith::DB. [msoulier MN00044891]

* Tue Jul 20 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-03]
- Undeprecated esmith::util::serviceControl. [msoulier MN00043056]

* Fri Jun 25 2004 Tony Clayton <apc@e-smith.com>
- [1.15.1-02]
- Merge language_tag2locale() function from perl-I18N-LangTags [tonyc
  MN00040170]

* Fri May 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.1-01]
- Rolling to collect patches.

* Fri May 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-23]
- Reordered the create code slightly to catch more errors.
  [msoulier MN00035059]

* Fri May 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-22]
- Added yet more error handling and reporting. [msoulier MN00035059]

* Fri May 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-21]
- Fixed one $Error reference that I missed in the last rev.
  [msoulier MN00035059]

* Fri May 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-20]
- Moved error handling from esmith::DB::db to esmith::DB, since it should not
  be database implementation specific. [msoulier MN00035059]

* Fri May 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-19]
- Propagated migration failures up to calling code for reporting to syslog.
- Propagated creation failures up to calling code. 
- Moved lexicon $Error in esmith::DB::db to a class property so it can be used
  by subclasses. [msoulier MN00035059]

* Thu May 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-18]
- Changed print statements to calls to the logger. [msoulier MN00035059]

* Thu May 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-17]
- Added print statements to initialize-default-databases for post-install
  debugging. [msoulier MN00035059]

* Fri May  7 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-16]
- Fixed migrate to report the caught error message. [msoulier MN00032503]

* Thu May  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-15]
- Added isValidHostname function to esmith::util::network.
  [msoulier MN00024212]

* Fri Feb 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-14]
- Greatly simplified the _mysystem function by ripping out open3.
  [msoulier dpar-20385]

* Fri Feb 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-13]
- Backed-out change in esmith::util, as it's non-trivial there with the exec.
  Completed update of esmith::event, and separated the esmith::Logger class.
  [msoulier dpar-20385]

* Fri Feb 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-12]
- Removed use of the logger entirely, replacing it with an abstracted
  interface to the Sys::Syslog module. [msoulier dpar-20385]

* Thu Jan  8 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-11]
- Fixed esmith::util::network::isValidIP() so valid IP substrings no longer
  return true values. [msoulier 9308]

* Thu Jan  8 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-10]
- Added a check in STORE in esmith::config for invalid attempts to set a value
  without a type. Also escalated previous warnings for undef key and value to
  fatal exceptions. [msoulier 7386]

* Thu Jan  8 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-09]
- Now trimming whitespace around keys and values during esmith::config STORE
  events, to prevent invalid keys and values from being saved. [msoulier 7021]

* Mon Jan  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-08]
- Fixed POD around merge_props. [msoulier 9482]

* Fri Nov  7 2003 Tony Clayton <apc@e-smith.com>
- [1.15.0-07]
- And again [tonyc 10569]

* Fri Nov  7 2003 Tony Clayton <apc@e-smith.com>
- [1.15.0-06]
- Change Merge API a bit, fix pod [tonyc 10569]

* Fri Nov  7 2003 Tony Clayton <apc@e-smith.com>
- [1.15.0-05]
- Add esmith::DB::Merge library [tonyc 10569]

* Fri Oct 10 2003 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-04]
- Fixed AccountsDB.pm to handle group names with hyphens and periods, to match
  the error message in the groups panel, and the rest of the group/user
  behaviour. [msoulier 10236]

* Sun Sep 21 2003 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-03]
- Skip any directries when iterating over action scripts in esmith::event.
  Add logfile timestamp symlinking to generic_template_expand action.
  Use templates2expand and logfiles2timestamp subdirectories of the event
  directory. Fix shebang line. [charlieb 10035]

* Thu Sep 18 2003 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-02]
- Add generic_template_expand action. [charlieb 10035]

* Thu Sep 18 2003 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-01]
- Changing version to development stream number - 1.15.0

* Tue Sep  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.14.1-01]
- Rebuild [gordonr 1305]

* Tue Sep  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.14.0-06]
- More Copyright cleanups [gordonr 1305, 9885]

* Tue Sep  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.14.0-05]
- Adjusted Copyright [gordonr 1305]

* Thu Aug 14 2003 Michael Soulier <msoulier@e-smith.com>
- [1.14.0-04]
- Added a test for the previous problem. [msoulier 9634]

* Thu Aug 14 2003 Michael Soulier <msoulier@e-smith.com>
- [1.14.0-03]
- Fixed error in esmith::templates causing $confref to not be set.
  [msoulier 9634]

* Fri Jun 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.14.0-02]
- Make create-system-user fallback to a system assigned UID if
  we couldn't get the one we wanted. [gordonr 9201]
- Don't explicitly call groupadd - useradd does that [gordonr 9201]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.14.0-01]
- Change to stable stream version number - 1.14.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.3-08]
- Changed reference to /etc/samba/smbpasswd [gordonr 9151]

* Tue Jun 24 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-07]
- Really fixed the logfile warning. [msoulier 9123]

* Tue Jun 24 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-06]
- Changed open mode for passwd and group files to read-only. 
  [msoulier 6033]
- Fixed a logfile warning. [msoulier 9123]

* Mon Jun  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-05]
- Added use of Unix::PasswdFile and Unix::GroupFile modules into uidgid.t.
  [msoulier 6033]

* Fri Jun  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-04]
- Added uidgid.t tests for testing compliance of uids and gids to chosen
  values. [msoulier 6033]

* Mon Jun  2 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-03]
- Untainting the result of readdir() on the migration directories.
  [msoulier 8878]

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-02]
- Added testing of forced values. [msoulier 3299]

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.3-01]
- Collecting patches into a new source tarball.

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-12]
- Modified initialize_default_databases to return a proper return value.
  [msoulier 3299]

* Wed May 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-11]
- Moving esmith::console from e-smith-base to e-smith-lib. [charlieb 8851]

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-10]
- Added an eval block around the key parts of the migrate method, to catch a
  fatal exception and permit processing to continue. [msoulier 8842]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-09]
- Added a test script for testing initialize-default-databases. It is not yet
  complete. [msoulier 3299]
- Fixed an error in esmith::db::_db_string_to_type_and_hash that handled a
  value of 0 improperly. [msoulier 3299]

* Mon May 26 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-08]
- Added a configurable dbhome and dbroot to initialize-default-databases, for
  testing purposes. [msoulier 3299]

* Mon May 26 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-07]
- Added an argument to initialize-default-databases, to take the db root as an
  argument. This is required for automated testing. [msoulier 3299]

* Fri May 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-06]
- Backing-out quad2bits and bits2quad functions, as we have this functionality
  already in esmith::util. [msoulier 8713]

* Fri May 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-05]
- Added an %EXPORT_TAGS section, with an all tag. [msoulier 8713]

* Fri May 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-04]
- Fixed an error in bits2quad, and exported the functions.
  [msoulier 8713]

* Fri May 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-03]
- Added quad2bits and bits2quad functions. [msoulier 8713]

* Mon May 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-02]
- Moved initialize_default_databases into esmith::util.
  [msoulier 8774]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.2-01]
- Sigh, and really rolling a new tarball [gordonr 5053]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-93]
- Rolling new tarball [gordonr 5053]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-92]
- Typo - s/LocalInterface/InternalInterface/ [gordonr 5053]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-91]
- Added esmith::ConfigDB::wins_server to centralise some logic [gordonr 5053]

* Thu May 15 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-90]
- Change create-system-user to warn if user exists and uid is not expected value,
  rather than die. [charlieb 6033]
- Add "use esmith::util" to the package environment for template expansion, within
  esmith::templates::processTemplate(). [charlieb 8671]

* Tue May  6 2003 Tony Clayton <apc@e-smith.com>
- [1.13.1-89]
- Fix get_all_by_prop() again - remove pipe boundries, add line-start boundry
  [tonyc 8372]

* Tue May  6 2003 Tony Clayton <apc@e-smith.com>
- [1.13.1-88]
- Fix get_all_by_prop() to include records if at least one value matches in
  multi-value properties [tonyc 8372]

* Fri May  2 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-87]
- Fixed bad return from computeLocalNetworkShortSpec in esmith::util.
  [msoulier 8578]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-86]
- Fixed a warning in esmith::util. [msoulier 8277]
- Fixed a bad call to Net::IPv4Addr. [msoulier 8277]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-85]
- Updated the EXPORT_OK list in esmith::util::network. [msoulier 8277]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-84]
- Added a cmpIP function in esmith::util::network. [msoulier 8277]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-83]
- Added dependency on perl-Net-IPv4Addr. [msoulier 8600]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-82]
- Made esmith::util use Net::IPv4Addr. [msoulier 8600]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-81]
- Corrected Copyright date [gordonr 8016]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-80]
- Genericise text in genHeader/genFooter - only a few panels still use these [gordonr 8016]
- Removed blocks of dead code [gordonr 8016]

* Mon Apr 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-79]
- Renamed method to avoid confusion with I18N::LangTags [gordonr 3793]

* Mon Apr 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-78]
- Added and updated tests in esmith:I18N [gordonr 3793]
- Force the locale for French and Spanish [gordonr 3793]

* Mon Apr 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-77]
- Fixed display of file contents that were not generated via multilog.
  [msoulier 6930]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-76]
- Added tests for record_has_defaults [gordonr 8535]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-75]
- There's no need to check for migrate fragments - they don't have
  standard names, and they will be files, not directories [gordonr 8535]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-74]
- And actually check the for the record's directories [gordonr 8535]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-73]
- Added record_has_defaults method [gordonr 8535]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-72]
- Added warnings for trying to store values that are undefined.
  [msoulier 7600]
- Returned immediately if value is not defined in IPquadToAddr.
  [msoulier 7600]
- Updated Copyright in initialize-default-databases [gordonr 3363]

* Wed Apr 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-71]
- Split esmith::Tai64n into a sub-package [gordonr 6930]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-70]
- Generate "ALL", not "127.0.0.1 ALL" for "public" access [gordonr 7729]

* Mon Apr  7 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-69]
- Call migrate() from create() to give scripts a chance to run [markk 7697]

* Mon Apr  7 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-68]
- Removed useless warnings and check for empty DB in migrate() [markk 7697]

* Fri Apr  4 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-67]
- Add create-system-user script to create users with known uid/gids.
  This provides shorthand for use in %pre sections of RPMs. We may
  need to do some dependency juggling to ensure that e-smith-lib is
  upgraded before the %pre script of other RPMs is run.
  [charlieb 6033]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [1.13.1-66]
- add CSS to esmith::cgi::genNameValueRow() [tonyc 7950]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-65]
- chgrp configdb files to admin on close [gordonr 2676]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-64]
- And rolled back the one in db.pm as well [gordonr 7987]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-63]
- Removed fatal exception on unsupported method - breaks inheritance.
  Could probably go back with a can() call [gordonr 7987]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-62]
- Chown config db files to root:admin [gordonr 2676]

* Wed Apr  2 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-61]
- Added strict checking of AUTOLOAD arguments, and fatal exceptions if
  unsupported methods are called. [msoulier 7987]

* Tue Apr  1 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-60]
- Clarify target, outputfile and tempfile usage in processTemplate, and 
  fix some corner case bugs. All selftests now pass. [charlieb 7717]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-59]
- Adjusted format of Tai64n::tai64nlocal [gordonr 6930]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-58]
- Added Tai64n::tai64nlocal [gordonr 6930]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-57]
- Added Copyright to Tai64n.pm [gordonr 6930]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-56]
- Added esmith::Tai64n.pm [gordonr 6930]

* Mon Mar 31 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-55]
- Use $processTemplate{Debug} to control stderr output from processTemplate.
  [charlieb 7717]

* Mon Mar 31 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-54]
- Use MD5 to determine whether templated files have changed, and only
  replace if they file is different. If required, use DebugTemplateExpansion
  to generate log noise as the decision is made. [charlieb 7717]

* Thu Mar 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-53]
- Make BACKGROUND=>false default for serviceControl() . [charlieb 7786]
- Allow genFooter() to take either a CGI or CGI::FormMagick object
  and do the right thing with the footer in both cases [gordonr 3553]

* Thu Mar 20 2003 Tony Clayton <apc@e-smith.com>
- [1.13.1-52]
- Add optional fourth argument "colspan" to esmith::cgi::genSmallCell() 
  [tonyc 7734]

* Wed Mar 19 2003 Tony Clayton <apc@e-smith.com>
- [1.13.1-51]
- Add new esmith::util::authenticateUnixPassword() function [tonyc 6030]

* Wed Mar 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-50]
- Added templates-default/template-end-php [gordonr 7360]
- processTemplate() now uses $OUTPUT_FILENAME for the path to the
  temporary file (rather than $TEMPLATE_PATH) [gordonr 5686]

* Mon Mar 17 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-49]
- Added language specific template-begin fragments [gordonr 7360]
- TODO: Remove all of the static copies - see bug 3295

* Mon Mar 17 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-48]
- Fix remaining test failure - we need to reopen the right DB file for
  migrate to work correctly. [charlieb 7713]

* Mon Mar 17 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-47]
- In processTemplate, define $confref to the CONFREF if that was passed
  in, and reference to confref from config db otherwise (as per pod).
  [charlieb 7299]
- Fix template.pm tests to expect $confref to always be defined.
  [charlieb 7713]
- Use scratch copy of database for migrate/defaults test cases, to avoid
  dirtying of db's starting values (which are from CVS). [charlieb 7713]

* Sun Mar 16 2003 Mike Dickson <miked@e-smith.com>
- [1.13.1-46]
- removed message in the top of the panel from showing up [miked 7676]

* Fri Mar 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-45]
- Delete templates-default/template-end - we often want nothing at all
  and the Jim Morrison/Apocalypse Now tag line isn't useful [gordonr 7702]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-44]
- Deal gracefully with empty and missing migrate directory, when setting
  up defaults using esmith::DB::migrate. [charlieb 7697]

* Thu Mar 13 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-43]
- Uncommented use of I18N::LangTags including language_tag2locale, since
  the code won't compile without it. [msoulier 1661]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-42]
- Add reload of db between running migrate fragments and setting of
  defaults.i See bugzilla for details. [charlieb 7652]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-41]
- Add $confref and value of each key as scalar to environment of all
  templates (as I believe was originally intended). This fixes various
  template breakage. TODO: fix some broken tests. [charlieb 7299]

* Mon Mar 10 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-40]
- Check group as well as passwd file in new_record [markk 1507]
- Added validate_account_name utility function. Can also be called as a 
  class method [markk 1507]
- Added tests for new_record (all tests pass) [markk 1507]

* Fri Mar  7 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-39]
- Added new_record subclass in esmith::AccountsDB [markk 1507]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-38]
- Update db initialisation code. Remove database files from rpm, and mark them
  "ghost" in spec file instead. [charlieb 1507]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-37]
- Update all properties together when setting defaults, to avoid excessive
  log file noise. [charlieb 1507]
- Change initialize-default-databases to create/update all databases for which
  defaults exist. Add the event to {bootstrap-,}console-save as well. [charlieb 1507]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-36]
- Gracefully handle missing migrate and defaults directories. [charlieb 1507, 3299]
- Add "accounts" to lists of dbs to initialize/migrate. [charlieb 1507]

* Mon Mar  3 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-35]
- Don't migrate an empty database [markk 3299]

* Mon Mar  3 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-34]
- Split up loadDefaults into two methods, migrate and _loadDefaults [markk
  3299]
- _loadDefaults now private [markk 3299]
- Added resetToDefaults method to force reset [markk 3299]
- Changed initialize-default-databases to be event-aware. Calls create in
  post-install and migrate in post-upgrade. [markk 3299]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-33]
- Add esmith::ConfigDB::hosts_allow_spec method for use in
  /etc/hosts.allow template fragments. [charlieb 5650]
- Update pod in esmith::{ConfigDB,util} to document new get_
  methods, and to note deprecated APIs.

* Thu Feb 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-32]
- Renamed computeLocalAccessSpec method to local_access_spec. Added
  "DEPRECATED" note to esmith::utils::computeLocalAccessSpec.
  [charlieb 5650]

* Thu Feb 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-31]
- Added unit tests in Config.pm and fixed some others [markk 3299]
- Create new method computeLocalAccessSpec in esmith::NetworksDB - which
  should be used instead of the function of the same name in esmith::utils.
  [charlieb 5650]
- Fix esmith::computeLocalAccessSpec to remove duplicate local network.
  [charlieb 5650]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-30]
- Handle fallbackLocale when calling setLocale() with only one
  argument (e.g. from the console) [gordonr 6997]

* Thu Feb 27 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-29]
- Cleaned up database creation in initialize-default-databases [markk 3299]

* Wed Feb 26 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-28]
- Added methods get_value_and_delete and get_prop_and_delete [markk 3299]
- Extended initialize-default-databases to create configuration and
  loadDefaults on all [markk 3299]

* Wed Feb 26 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-27]
- Fix a bug in 00openRW creation [markk 3299]

* Wed Feb 26 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-26]
- Changed loadDefaults to process migrate dir en masse [markk 3299]
- Create 00openRW fragment in all db migrate dirs [markk 3299]

* Wed Feb 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-25]
- First shot at loadDefaults. [markk 3922]
- Expanded POD in loadDefaults [gordonr 3922]
- Added $ENV{ESMITH_DB_DEFAULTSDIR} override to loadDefaults [gordonr 3922]
- First pass at updating the POD documentation. Much yet to do. [msoulier 2128]
- Back out templates-local changes [gordonr 7233]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-23]
- Removed any references to LocalDomainPrefix. [msoulier 4812]

* Fri Feb 21 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-22]
- Remove legacy WebServerName setting from test configuration data. [charlieb 6861]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-21]
- Added get_value() and get_prop() methods to esmith::DB so you can
  do $configdb->get_value("EthernetAssign") and 
  $configdb->get_prop("sshd","status") without using temporaries
- Added tests for these methods on ConfigDB.pm
- Adjusted Copyright notices and AUTHOR details [gordonr 6501]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-20]
- Make config dbs 0660, not 0600 [gordonr 2676]

* Thu Feb 20 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-19]
- Removed dead options processing code from event_signal. [charlieb 4912]

* Mon Feb 17 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-18]
- Added templates-local to processTemplate queue [markk 7233]

* Mon Feb  3 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-17]
- Explicitly creating db files in the specfile. [msoulier 6886]

* Thu Jan 30 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-16]
- Gathering patches into a new tarball.

* Tue Jan 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-13]
- Fix variable name error in esmith::AccountsDB::get_next_uid() [charlieb 6367]

* Tue Jan 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-12]
- Search for bunch more places for NIC drivers in esmith::ethernet.
  This will catch in particular tulip, e100 and e1000. [charlieb 5617]

* Mon Jan 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-11]
- Change Copyright tag to License: GPL.
- Fix logical inversion in error checking of db file write. [charlieb 6248]

* Wed Jan 22 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-10]
- Add error checking at each step of writing out db files. [charlieb 6248]
- Fix esmith::AccountsDB::get_next_uid to use set{pw,gr}ent/end{pw,gr}ent.
  [charlieb 6367]

* Mon Jan 20 2003 Mike Dickson <miked@e-smith.com>
- [1.13.1-09]
- added mergeDB [miked 6670]

* Thu Jan 16 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-08]
- Actually use the argument passed to setLocale [markk 3357]

* Thu Jan 16 2003 Mark Knox <markk@e-smith.com>
- [1.13.1-07]
- Added LC_ALL to setLocale() for date formatting [markk 3357]

* Fri Jan  3 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-06]
- Modified setLocale() to take an optional third argument, which can be either
  a language tag or a locale, to permit explicitely setting the locale instead
  of having the method determine it independently. [msoulier 5212]

* Fri Jan  3 2003 Mike Dickson <miked@e-smith.com>
- [1.13.1-05]
- and update the spec file again since the first attempt failed to build [miked]

* Fri Jan  3 2003 Mike Dickson <miked@e-smith.com>
- [1.13.1-04]
- removed function prototypes [miked 6397]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-03]
- Backing out the pam-pam_smbpass change for now. It's not properly
  handling addition/deletion of users and it's probably not all that
  bad to keep smbpasswd around [gordonr 6388]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-02]
- Removed calls to smbpasswd in setPassword() and removed dependency 
  on Samba since we now use pam-pam_smbpass. Added a dependency on
  pam-pam_smbpass - it's not strictly true, but will stop people from
  installing this version of e-smith-lib only to find smbpasswd entries
  not being maintained. 
  TODO: Remove now obsolete samba password routines [gordonr 6388]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-01]
- Missed some test directories from the last import, and ignore CVS
  directories when peforming readdir calls in tests [gordonr 5212]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-09]
- New library esmith::I18N with various I18N routines:
  available{Languages,Locales}
  preferred{Language,Locale}
  fallback{Language,Locale}
  setLocale [gordonr 5212]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.13.0-08]
- removed telnet warning [miked 6216]
- fixed a few typos in a few functions [miked]
- added the ability for genCell to accept a class name [miked 5494]

* Tue Dec 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-07]
- Make "actions" an invalid event. [charlieb 5642]

* Mon Dec 16 2002 Mike Dickson <miked@e-smith.com>
- [1.13.0-06]
- UI Update, part of the tweaking for the new UI [miked 5494]

* Wed Dec  4 2002 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-05]
- Added the isValidPort function. [msoulier 6061]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [1.13.0-04]
- ui update  [miked 5494]

* Fri Nov 29 2002 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-03]
- Enhanced the IP address validation in isValidIP(). [msoulier 5937]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.13.0-02]
- update to new UI system [miked 5494]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [1.13.0-01]
- Changing to development stream; version upped to 1.13.0

* Fri Nov  1 2002 Michael Soulier <msoulier@e-smith.com>
- [1.12.1-02]
- Fixed broken AUTOLOAD resulting in broken services() method.
  [msoulier 5460]

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.12.1-01]
- Roll new version to fix tagging problem

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-01]
- Roll to maintained version number to 1.12.0

* Thu Oct 10 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.11-06]
- Sort output of get_all_by_prop (alphabetically by key) [charlieb 4944]

* Thu Oct  3 2002 Tony Clayton <apc@e-smith.com>
- [1.11.11-05]
- fix bogus autovivification of network card hash entries for non-ethernet pci
  devices in ethernet.pm [tonyc 4191]

* Wed Oct  2 2002 Mark Knox <markk@e-smith.com>
- [1.11.11-04]
- Carp about and fix up calls to get_all_by_prop that supply a hash 
  [markk 3786]

* Thu Sep 26 2002 Mark Knox <markk@e-smith.com>
- [1.11.11-03]
- serviceControl is a successful NOP without ORDER property [markk 4963]

* Thu Sep 26 2002 Mark Knox <markk@e-smith.com>
- [1.11.11-02]
- Removed some verbosity from serviceControl [markk 4963]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.11-01]
- Prep for --as-source build, to work around a problem with co2rpm.

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.10-06]
- Remove {create,remove}_user_pseudonyms method in esmith::AccountsDB,
  and add {create,remove}_user_auto_pseudonyms and remove_all_user_pseudonyms
  methods. Update some tests and documentation. [charlieb 4669]

* Thu Sep 12 2002 Mark Knox <markk@e-smith.com>
- [1.11.10-05]
- Whoops.. include the path in symlink() [markk 4860]

* Thu Sep 12 2002 Mark Knox <markk@e-smith.com>
- [1.11.10-04]
- Add serviceControl enable and disable functionality back in for
  backwards compatibility. They are still deprecated. [markk 4860]

* Mon Aug 26 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.10-03]
- Add open_ro method to esmith::{Networks,Domains,Hosts}DB.
  so that open_ro without filename succeeds using default. [charlieb 3397]

* Mon Aug 26 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.10-02]
- Add open_ro method to esmith::AccountsDB so that open_ro without
  filename succeeds using default. [charlieb 3397]

* Wed Aug 21 2002 Mark Knox <markk@e-smith.com>
- [1.11.10-01]
- Instruct Text::Template to untaint program text [markk 4138]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.9-01]
- Make expand-template show usage if no arg is given [charlieb 4570]
- Remove any rc7.d symlink handling from serviceControl(). No longer
  insist on "ORDER" param. Deprecate enable/disable/delete as these
  are now all NOOPs. [charlieb 4458]
- Unlink empty output file if no templates are found [charlieb 4578]

* Tue Aug 13 2002 Tony Clayton <apc@e-smith.com>
- [1.11.8-02]
- differentiate between warnings and errors in processTemplate [tonyc 4143]
- use carp/croak instead of warn/die in processTemplate [tonyc 4143]
- use goto to call processTemplate from esmith::util [tonyc 4143]
- add ERROR/WARNING/DEBUG prefixes to processTemplate messages [tonyc 4143]

* Wed Aug  7 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.8-01]
- Roll back split RE change in ethernet.pm. [charlieb 4166]
- Allow ConfigDB->open_ro to use implicit filename. [charlieb 3397]
- Allow ConfigDB->open to succeed in r/o mode if file is not writable
  by user doing the opening. [charlieb 4417]
  TODO: tests to be added/updated.

* Wed Jul 24 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.7-01]
- Relax split RE in ethernet.pm, from \t to \s+ to handle pcitable
  file in RedHat 7.3. [charlieb 4166]

* Thu Jul 18 2002 Tony Clayton <apc@e-smith.com>
- [1.11.6-01]
- throw errors to STDERR and die in processTemplate [tonyc 4143]

* Wed Jul 17 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.11.5-01]
- Fixed syntax in the 1.11.4 change below - missing paren [gordonr 4166]

* Tue Jul 16 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.4-01]
- Use /usr/share/hwdata/pcitable if we find it (in ethernet.pm), otherwise
  fall back to /usr/share/kudzu/pcitable. [charlieb 4166]

* Wed Jul 10 2002 Mark Knox <markk@e-smith.com>
- [1.11.3-01]
- Check that @args is defined before calling "isa" on it [markk 4150]
- Pass the right arguments to events and actions [markk 3245]

* Wed Jul 10 2002 Mark Knox <markk@e-smith.com>
- [1.11.2-01]
- Added options processing to signal-event to allow logging of server-ID and
  IP address [markk 4150]

* Fri Jul  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-01]
- Add $! to die() message if template file rename fails. Also
  remove comment about atomicity of rename operation, which
  seems to be wrong. [charlieb 2292]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Changing version to maintained stream number to 1.11.0

* Sun Jun  2 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.2-01]
- Fix naive adding of users to groups. We need to remove duplicates,
  and handle empty list correctly. [charlieb 3773]

* Sun Jun  2 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.10.1-01]
- Strip pipes from properties - it's not safe to cook them while there
  is code which expects to be able to split on pipe [gordonr 3785]

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to maintained stream number to 1.10.0

* Fri May 31 2002 Mark Knox <markk@e-smith.com>
- [1.9.58-01]
- Setuid to the requesting user in setUnixPasswordRequirePrevious so that PAM
  will prompt for the current password [markk 3767]

* Thu May 30 2002 Tony Clayton <apc@e-smith.com>
- [1.9.57-01]
- s/use/require/ for Exporter and IO::File in templates.pm [tonyc 3749]

* Tue May 28 2002 Mark Knox <markk@e-smith.com>
- [1.9.56-01]
- minor fix to esmith::util::link pod [tonyc 3580]
- remove unneeded END block in esmith::util::link [tonyc 3580]
- move tmp fifo file to /tmp in esmith::util::link [tonyc 3580]
- force system-created pseudonyms to lowercase [markk 3692]

* Mon May 27 2002 Tony Clayton <apc@e-smith.com>
- [1.9.55-01]
- added esmith::util::link package, with getExternalLink() function [tonyc 3580]

* Sat May 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.54-01]
- s/ESMITH_HOSTS_DB/ESMITH_DOMAINS_DB/ in DomainsDB.pm [gordonr 3647]

* Fri May 24 2002 Tony Clayton <apc@e-smith.com>
- [1.9.53-01]
- s/prop()/prop('type')/ in get_next_uid() [tonyc 3664]

* Fri May 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.52-01]
- Check that the property exists before trying to test it in
  get_all_by_prop [gordonr 3647]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.51-01]
- RPM rebuild forced by cvsroot2rpm

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.50-01]
- Log status value of any action script which returns non-zero status
  to event_signal(). [charlieb 3555]
- Do not log message when open of db fails in config.pm, only do so
  if db exists but is not readable. [charlieb 3562]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.49-01]
- Add CONFREF back into expand-template and use the esmith::util
  version of processTemplate() so that all fragments get the 
  namespace of esmith::util for free. Templates should not assume
  this, but some existing ones do [gordonr 3272]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.48-01]
- Rebuilding as the wrong version of esmith::templates was tagged
  [gordonr 3404]

* Sat May 18 2002 Mark Knox <markk@e-smith.com>
- [1.9.47-01]
- Moved get_next_uid from useraccounts panel to AccountsDB [markk 3404]

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.46-01]
- Make locking code NOOP under perl 5.6.0, and relax perl version
  dependency [charlieb]
- Skip locking tests if running under perl 5.6.0 [charlieb]

* Fri May 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.45-01]
- Fix a typo in esmith::ConfigDB::getLocale. [charlieb 3120]

* Thu May 16 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.44-01]
- esmith::NetworksDB docs had the wrong default file [schwern 3474]

* Wed May 15 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.43-01]
- Removing DBS feature from processTemplate() and expand-template
  [schwern 3272]
- Fixing order of template queue processing [schwern 3441]
- Adding esmith::DB->open_ro() [schwern 3397]
- Changing $esmith:DB::Error to esmith::DB->error.  Much easier for
  all the esmith::DB subclasses to deal with. [schwern 3397]

* Thu May  9 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.42-01]
- Removing incorrect docs about locking being disabled [schwern 2674]
- Fixing changing locking tests to match the change in 1.9.41
  [schwern 2674]

* Wed May  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.41-01]
- Remove file locking in TIEHASH method of Config.pm - it's not
  necessary (_writeconf creates a new file, and hence doesn't write
  to the existing one) [charlieb 2674]

* Wed May  8 2002 Tony Clayton <apc@e-smith.com>
- [1.9.40-01]
- return undef instead of 0 for esmith::ConfigDB::{new_record,get} and
  esmith::DB::db::open [tonyc 3252]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.39-01]
- Fixed call to ->prop() in determineRelease() [gordonr 2297]

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.38-01]
- Grab e-smith-release from sysconfig|ReleaseVersion instead of doing
  a runtime rpm query [gordonr 2297]

* Fri May  3 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.37-01]
- Reinstating locking code disabled in 1.9.7-01. [schwern 2674]
- Upping minimum perl to 5.6.1 so the locking code will work [schwern 2674]

* Fri May  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.36-01]
- Changed website URL to www.mitel.com [gordonr 3235]

* Tue Apr 30 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.35-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]
- Added esmith::DB->as_hash [schwern 3272]

* Wed Apr 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.34-01]
- Ensuring templates are sorted regardless of locale [schwern 3225]

* Mon Apr 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.33-01]
- Create empty /home/e-smith/hosts in post-install [gordonr 3045]

* Fri Apr 19 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.32-01]
- Created esmith::util::network [schwern 3080]

* Fri Apr 19 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.31-01]
- Added propogate_hosts() and hosts() to esmith::HostsDB [schwern 3045]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.30-01]
- Don't require PAM authentication if we are already root. This allows
  root to set the root/admin password from the bootstrap-console [gordonr]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.29-01]
- Updates to esmith::Util to make it actually check the old password when doing
  a set.*PasswordRequirePrevious call. [adrianc]
- getLicense can take a language tag, defaulting to server locale [gordonr 3119]

* Tue Apr 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.28-01]
- Updated getLicenses() to be locale aware [gordonr 3119]

* Tue Apr 16 2002 Mark Knox <markk@e-smith.com>
- [1.9.27-01]
- Added new ConfigDB method 'getLocale()'. Fetches lang/kbd settings.
  [markk 3120]

* Wed Apr 10 2002 Adrian Chung <adrianc@e-smith.com>
- [1.9.26-01]
- Modify postinstall script to not bark when attempting removal of 5.005/esmith
  directory.

* Wed Apr 10 2002 Michael Schwern <schwern@e-smith.com>
- [1.9.25-01]
- Added rsync() and rsync_ssh() to esmith::utils::system [schwern]

* Wed Apr 10 2002 Adrian Chung <adrianc@e-smith.com>
- [1.9.24-01]
- Alter esmith::AccountsDB::activeUsers() to return a list instead of a count,
  which we can get using scalar. [mac #3134]

* Wed Apr 10 2002 Adrian Chung <adrianc@e-smith.com>
- [1.9.23-01]
- Add esmith::AccountsDB::activeUsers() routine to AccountDB.pm [mac #3134]

* Fri Apr  5 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.22-01]
- Cleaning up uses of dummy test files so they use scratch copies [schwern]
- Added a warning to merge_props() and reset_props() to guard against
  accidentally passing a hash ref. [schwern]

* Fri Apr 05 2002 Jason Miller <jmiller@e-smith.com>
- [1.9.21-01]
- processTemplate() now won't add the default template-begin to a
  single file template [schwern 3110]
- Add action initialize-default-databases to post-{install,upgrade}
  so that databases are created on initial installation [jay]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.20-01]
- Added esmith::NetworksDB [skud 3027]
- Added esmith::DomainsDB [skud 3032]
- Adjusted documentation in templates.pm to match changes in
  httpd.conf/VirtualHosts [gordonr]

* Thu Mar 28 2002 Kirrily Robert <skud@e-smith.com>
- [1.9.19-01]
- added esmith::AccountsDB::set_user_groups() [skud]

* Tue Mar 26 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.18-01]
- Finishing touches on processTemplate's DBS & MORE_DATA. [schwern 3083]

* Tue Mar 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.17-01]
- Suppress "Skipping" warning on subdirectories in processTemplate() [gordon]
- Added DBS & MORE_DATA to esmith::templates::processTemplate.
  Deprecated CONFREF. [schwern 3083]
- esmith::DB::Record->props now returns the # of properties in scalar
  context. [schwern 3083]

* Wed Mar 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.16-01]
- Added computeAllLocalNetworkPrefixes() function to util.pm, for
  use for tinydns and dnscache access lists [charlieb]
- Added tests for new code in util.pm
- Fixed test failures in DomainDB module.

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.15-01]
- Breaking circular dependency between e-smith-lib and e-smith-test
  by making e-smith-test a build requirement [schwern]
- That means we'll need e-smith-test on lamington, eh? (It's really
  BuildVeryDesirable rather than BuildRequires).
- Added a DomainsDB [charlieb]

* Wed Mar 13 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.14-01]
- esmith::ConfigDB::Record did not get released with 1.9.13 [schwern 3026]
- esmith::HostsDB test was looking for the wrong host [schwern]

* Tue Mar 12 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.13-01]
- Fixing and testing esmith::templates::removeBlankLines [schwern 2130]
- esmith::config::CLEAR wasn't clearing the tied hash [gordonr 2885]

* Mon Mar 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.12-01]
- Remove recursion from _merge_templates function [tonyc 1799]
- Skip all subdirectories inside template directories

* Tue Mar  5 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.11-01]
- Fixed behavior of typeless esmith::DB::db records [schwern 2937]
- Added esmith::DB->reload [schwern 2938]
- Really removing legacy 5.005 directory [schwern]
- Added esmith::util::system [schwern]

* Fri Mar  1 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.10-01]
- Fixed warnings with undefined properties. [schwern]
- Removing legacy 5.005 directory [schwern]

* Fri Mar  1 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.9-01]
- Fixed a bug in get($key_that_doesnt_exist) from 1.9.8-01 [schwern]

* Thu Feb 28 2002 Michael G Schwern <schwern@e-smith.com>
- [1.9.8-01]
- Added value/set_value() to esmith::ConfigDB [schwern]

* Wed Feb 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.7-01]
- Added esmith::DB and esmith::DB::Record abstract interfaces to
  E-Smith databases. [schwern]
- esmith::config's locking has been disabled because of a bug in perl
  5.6.0 [schwern]
- Fully documented & tested esmith::db. [schwern]
- Deprecated esmith::db. [schwern]
- Changed esmith::GenericDB to esmith::DB::db plus more major API
  changes.  Now stable. [schwern]

* Tue Feb 26 2002 Kirrily Robert <skud@e-smith.com>
- [1.9.6-01]
- Added various routines to esmith::AccountsDB for handling groups and
  pseudonyms [skud]
- major API changes to esmith::GenericDB (see perldoc) [schwern]
- added esmith::config->filename() [schwern]

* Mon Feb 25 2002 Mark Knox <markk@e-smith.com>
- [1.9.5-01]
- now generates its own test suite using buildtests [skud]
- config.pm now falls back to the ESMITH_CONFIG_DB environment variable
  [skud]
- documented esmith::templates::processTemplate a bit [schwern]
- fixed bug introduced in 1.9.4, esmith::config was not generating
  new config files [schwern]
- fixed another bug introduced in 1.9.4, esmith::config's locking
  was a little off [schwern]
- fixed bug introduced in 1.9.4, esmith::templates::processTemplate was not
  using filters properly for OUTPUT_TYPE='string' invocations. [tonyc]
- Move any files from legacy directory /usr/lib/perl5/site_perl/5.005/esmith
  to new location /usr/lib/perl5/site_perl/esmith [markk]
- removed a bug fix introduced in 1.9.4 as it broke scripts using taint
  [schwern 2878]
- must use absolute path on buildtests call [markk]

* Tue Feb 19 2002 Tony Clayton <tonyc@e-smith.com>
- [1.9.4-01]
- rolled to 1.9.4 
- refactoring and test suite for esmith::config and esmith::templates
  [skud/schwern]
- processTemplate now has an OUTPUT_TYPE=>'string' mode that returns the
  template text instead of writing it to a file. [tonyc #1799]
- fixed template namespace partitioning in processTemplate [tonyc]

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [1.9.3-01]
- rolled to 1.9.3 manually in CVS

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [1.9.2-01]
- rollRPM: Rolled version number to 1.9.2-01. Includes patches up to 1.9.1-02.

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [1.9.1-02]
- removed unnecessary rmdir from prep section of specfile

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [1.9.1-01]
- rollRPM: Rolled version number to 1.9.1-01. Includes patches up to 1.9.0-07.

* Wed Jan 9 2002 Peter Samuel <peters@e-smith.com>
- [1.9.0-07]
- Copyright notices modified to use the long form of the Mitel Networks
  Corporation copyright notice.
- Copyright notice added to files from which it was missing.
- Copyright date set to 2002.

* Mon Dec 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-06]
- Make sure that %pre script never returns an error status.

* Mon Dec 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Fix error in order of parameters to setUnixPasswordRequirePrevious.

* Mon Dec 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Fix typo in password changing function.
- Add missing / in kernel modules path in ethernet.pm.
- Fix test for legacy symlink in %pre script.

* Mon Dec 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Obsolete "autopasswd" and use Authen::PAM for password changes.

* Mon Dec 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Handle 2.4.x kernels in ethernet.pm; driver modules are in
  kernel/drivers/net subdirectory.
- Remove dangling /usr/lib/perl5/site-perl/5.005 directory.

* Mon Dec 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- rollRPM: Rolled version number to 1.9.0-01. Includes patches up to 1.8.0-01.
- Move e-smith directory into site-perl directory, rather than 5.005/site-perl.
  Remove site-perl/esmith symlink if necessary.
 

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.8.0-01]
- rollRPM: Rolled version number to 1.8.0-01. Includes patches up to 1.7.0-31.

* Fri Nov 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-31]
- Mitel branding for esmith::config database headers
- Adjusted Copyright

* Wed Nov 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-30]
- Remove troublesome e-smith-base dependency - it's not real anyway.

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-29]
- processTemplate: Guard oct() conversion of PERMS

* Tue Nov 20 2001 Kirrily Robert <skud@e-smith.com>
- [1.7.0-28]
- Minor documentation updates, especially to esmith::templates
- Bugfix in esmith::AccountsDB for where it wasn't correctly picking up 
  user/ibay/etc lists 

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-27]
- processTemplate: Call oct() on any passed PERMS value in case we get a string

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-26]
- Relocated esmith::util::processTemplate() to esmith::templates, leaving stub
- Changed package scope for esmith::templates (was esmith::util::templates)
- Adjusted Copyright notices

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-25]
- Back out patch in 1.7.0-22 - changing /etc/smbpasswd to 0600,admin,root
  allows "admin" to create machine accounts and means "root" is not required
  in /etc/smbpasswd

* Fri Nov 16 2001 Tony Clayton <tonyc@e-smith.com>
- [1.7.0-24]
- add div tags back into esmith::cgi for spacing body and images
- looks good in Netscape/Mozilla/IE5/Konqueror/Opera

* Fri Nov 16 2001 Tony Clayton <tonyc@e-smith.com>
- [1.7.0-23]
- localize $_ variable in esmith::config::readconf to avoid 'Modification of
  read-only value' error in perl 5.6.0

* Wed Nov 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-22]
- Set "root" password in smbpasswd when system password is set
- Unfortunately, Samba 2.2.2 will only allow "root" to create machine accounts

* Tue Nov 13 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-21]
- Add genSmallCellRightJustified and genSmallCellCentered to cgi.pm.

* Fri Nov 09 2001 Tony Clayton <tonyc@e-smith.com>
- [1.7.0-20]
- added lockfile.pm module (esmith::lockfile)

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-19]
- Reverted frame layout changes from [1.7.0-05]
- Adjusted Copyright
- Removed more DIV tags

* Wed Oct 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-18]
- Mitel branding changes.

* Mon Oct 29 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-17]
- Add four new perl modules. Three from Skud for adding OO access to
  config and accounts data bases, plus a new templates library containing
  a copy of processTemplate(), plus a sample filter function.

* Fri Sep 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-16]
- Add a guard before newline substitutions to catch undefined values;

* Wed Sep 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-15]
- Escape newlines in properties - convert to "\\n" when storing, and then
  reverse the process on restoration.

* Mon Sep 10 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-14]
- Removed db_open/db_close
- Guarded most warn calls on $esmith::db::DEBUG
- Protect reference counting from underflow

* Wed Sep 05 2001 Tony Clayton <tonyc@e-smith.com>
- [1.7.0-13]
- Fixed OO code in esmith::db
- cacheing should probably be moved to esmith::config
- db_open/db_close should probably go away

* Tue Sep 04 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-12]
- Add missing destructor for db object
- Remove object methods from export list
- Rework db command to use db object and object methods

* Tue Sep 04 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-11]
- Use package global variable $esmith::db::AUTOLOAD, not $AUTOLOAD
- Correctly handle empty value in private_db_string_to_type_and_hash()

* Tue Sep 04 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-10]
- Replace accessor functions with AUTOLOAD function
- Change private_db_path so that it leaves any absolute path unchanged

* Tue Sep 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-09]
- Fixed typo in print_prop

* Tue Sep 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-08]
- Provided OO versions of all routines
- Rewrite db_open/db_close to use OO versions open/close
- Redid reference counting using esmith::db objects

* Tue Sep 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-07]
- Added reference counting to db_open/db_close.
- OO interface untested and incomplete

* Tue Sep 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-06]
- Added initial db_open and db_close routines and their OO counterparts
  open and close. Need to add reference counting to db_open and db_close

* Fri Aug 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-05]
- Revised manager frame layout
- Removed some DIV tags, which aren't rendered properly in Konqueror and IE3

* Thu Aug 30 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-04]
- Pick up default template-begin, if there is not one already found

* Thu Aug 30 2001 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-03]
- Add a FILTER => coderef option to processTemplate, to allow
  convenient postprocessing of output.

* Wed Aug 29 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-02]
- Added optional argument --output_filename={pathname} to 
  /sbin/e-smith/expand-template. Argument can be shortened to -o {pathname}

* Wed Aug 29 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-01]
- Rolled version number to 1.7.0-01. Includes patches upto 1.6.0-09.

* Mon Aug 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.6.0-09]
- Added Vendor tag

* Mon Aug 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.6.0-08]
- Fixed dependency on e-smith-base version

* Fri Aug 17 2001 Tony Clayton <tonyc@e-smith.com>
- [1.6.0-07]
- fixed db_get_prop to return empty list if no $prop or $val

* Fri Aug 17 2001 gordonr
- [1.6.0-06]
- Autorebuild by rebuildRPM

* Tue Aug 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.6.0-05]
- Removed the 3.0 -> 4.0 upgrade kludge entirely
  Upgrades from 3.x to 5.x must go through 4.x

* Tue Aug 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-04]
- Fix logic error in check for accounts which should be system accounts -
  I corrected the code after I c&p into Bugzilla, but forget to fix the
  code I was editing.
- Do not print warning about PasswordSet value unless it is defined and not
  "yes".
- Use esmith::db functions to check PasswordSet value.

* Tue Aug 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-03]
- Fix perl problem in the reading of the accounts hash into %accounts.
  Apparently the code police doesn't check library code :-(

* Tue Aug 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-02]
- Check if db file exists but is not readable. If so, log error message and
  refuse to update it (with necessarily incomplete information).
- Prepend warning text message to db files when writing them.
- Do not update accounts db from cgi.pm. Change the conditions under which
  warning text is printed.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Rolled version number to 1.6.0-01. Includes patches upto 1.5.0-62.

* Thu Aug 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-62]
- Changed image format

* Tue Jul 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-61]
- Removed misplaced pod =cut directive

* Tue Jul 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-60]
- Added esmith::util::getLicenses()

* Tue Jul 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-59]
- More branding changes for cgi.pm for footer and navigation image

* Tue Jul 31 2001 Jason Miller <jmiller@e-smith.com>
- [1.5.0-58]
- More branding changes to cgi.pm to:
	- s/March Networks Server manager/March Networks SME Server
	  manager/
	- Remove the (c) in copyright statement
	- Move the copyright notice in genFooter() into two lines 

* Tue Jul 31 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-57]
- Changing stylesheet reference in cgi.pm from /server-manager
  to unauthenticated area /server-common

* Sun Jul 29 2001 Jason Miller <jmiller@e-smith.com>
- [1.5.0-56]
- Branding text changes to cgi.pm for <TITLE> and <IMG> tags 

* Fri Jul 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-55]
- Change style sheet path to /server-manager/css/manager.css
- Change e-smith-common to server-common.
- Change e-smith-brand to server-brand.

* Thu Jul 26 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-54]
- Change genFooter() for new branding

* Tue Jul 24 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-53]
- Changed cgi.pm to accomodate new e-smith-logo (March)

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.5.0-52]
- Changed license to GPL

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-51]
- Added patch from 1.5.0-50

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-50]
- Removed group/other access to configuration db fragments

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-49]
- [gen]LdapPassword() now warn (was die) on failures and return undef

* Wed Jun 27 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-48]
- Deprecated array version of determineRelease

* Thu Jun 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-47]
- Removed eval of Perl event handlers from signal-event - all handlers
  are called using the same system() interface

* Tue Jun 19 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-46]
- Tidy up code and documentation for genLdapPassword(), refactor to
  LdapPassword() and genLdapPassword(), and remove redundent newline
  from ldap.pw file.

* Mon Jun 18 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-45]
- Choose much stronger LDAP/MySQL password.

* Tue Jun 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-44]
- Changed log format - removed irrelevant PID and pathname

* Tue Jun 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-43]
- Added Start/End/Elapsed time logs for actions

* Thu Jun 07 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-42]
- Changed case of Copyright and All in footer

* Thu Jun 07 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-41]
- Added esmith::util::determineRelease - provides release number in
  scalar context and product name/release in array context. Moved
  from /sbin/e-smith/console
- Added product name to manager footers

* Mon Jun 04 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-40]
- When detecting ethernet cards, defer test for "Class 0200" until
  after looking up pcitable driver. If it's there, believe it.

* Sun Jun 03 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-39]
- fixed code in event.pm that saved STDERR and STDOUT under opposite names

* Fri Jun 01 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-38]
- override 'exit' function with die instead of return

* Fri Jun 01 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-37]
- Use rename() rather than system("mv", "-f" ...) to replace output
  file. This is well tested in 4.1.2, but was missed in the forward
  porting of 4.1.x updates.

* Thu May 31 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-36]
- remove Text::Template change from 1.5.0-34. needs debugging.

* Thu May 31 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-35]
- strip '\n' from return in esmith::event::exit

* Thu May 31 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-34]
- removed concurrency code for 5.0beta2
- pass copy of hash to Text::Template instead of reference (from patch 28)
- untaint data in esmith::config::readconf
- use temporary file in esmith::config::writeconf
- re-read esmith::config hash before changing/writing it in STORE and DELETE
- close dangling temporary filehandles in esmith::event
- override 'exit' function with return instead of die

* Wed May 30 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-33]
- re-add patches 23-27.
- pass copy of hash to Text::Template instead of reference (patch 28)
- detect possible deadlocks in esmith::config and die (patch 29)
- use a global cached copy of the hash (patch 30)
- tie read-only when called from template fragment (patch 30)

* Mon May 28 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-32]
- removed patches 23-27 for now to provide a stable image

* Mon May 28 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-31]
- removed previos patch (patch 27) for now to debug it

* Mon May 28 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-30]
- remove shared %esmith::config::CONFIG hash for now - causes trouble when
  trying to close tied hashes with more than one open reference
- only write out to file in esmith::config::DESTROY method, and only if changes
  occurred

* Mon May 28 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-29]
- uncomment RCSFILE parameter from esmith::config call to UnlockRCS

* Mon May 28 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-28]
- standardized calls to rcs/ci/co: always pass FILE, and pass RCSFILE if it is
  defined.  This also fixes a previous ci problem.

* Mon May 28 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-27]
- fixed RCSLock for case where config file doesn't already exist
- improved STDOUT redirecting code in RCSLock, RCSUnlock

* Sat May 26 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-26]
- added strict locking and RCS logging to all config files tied using
  esmith::config

* Wed May 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-25]
- removed UnsavedChanges flag code from esmith::config (now in e-smith-base)

* Wed May 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-24]
- verified patches 17,19 to work, leaving them in
- fixed some event.pm code for taint checks
- event_signal still can't be called with -T, but leaving for now

* Wed May 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-23]
- re-added patches 17,19 to debug post-install issues

* Thu May 10 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-22]
- Changed mailto tag in page headers

* Fri May 04 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-21]
- backed out signal-event and event_signal patches (17,19) for now to
  determine whether they broke post-install.

* Thu May 03 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-20]
- reverse exitcode for event_signal, and update signal-event
- added comments in event.pm for taint problems

* Wed May 02 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-19]
- override exit function in event handlers instead of s/exit/return/ stuff
- restore old STDOUT/STDERR filehandles before event-signal returns
- event-signal function returns on completion instead of exiting
- each template now gets expanded in a unique package namespace, shared by all
  fragments
- pre-load esmith::db into each template's package
- add '$confref' hash reference into each template's package

* Thu Apr 26 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-18]
- removed leading space in each line of action script in event.pm
- changed s/exit/return/ to be smarter about leaving 'exit' alone in plain text
  contexts

* Wed Apr 25 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-17]
- Remove local pcitable, and references to it in code.

* Thu Apr 19 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-16]
- added some padding for branded logo images.

* Thu Apr 12 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-15]
- fixed serviceControl substitution typo (changed = to =~)

* Wed Apr 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-14]
- computeHostsAllowSpec now returns as array if called in array context. The
  zeroth element is the service name tag (or a comment is the service is
  disabled). All other elements are those which are allowed access

* Wed Apr 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-13]
- serviceControl now handles an optional 'd' for ACTION of (en|dis)able[d]

* Tue Apr 10 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-12]
- forced signal event to send STDIN/STDERR to syslog

* Tue Apr 10 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-11]
- computeLocalAccessSpec now returns a space (was comma) separated list. This
  makes the return suitable for use in httpd.conf. This also modifes the
  returned string from computeHostsAllowSpec - hosts.allow and smb.conf
  are happy with commas or space, whereas httpd.conf will only accept spaces

* Mon Apr 09 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-10]
- Added co-dependency on e-smith-base version

* Mon Apr  9 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-09]
- More changes to cgi.pm for look and feel.
- Update esmith::util::computeLocalAccessSpec to understand
  "public" access.

* Mon Apr  9 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-08]
- Changes to cgi.pm for new manager look and feel.

* Mon Apr 09 2001 Gordon Rowell <gordonr@e-smith.com
- [1.5.0-07]
- Added optional access parameter to computeLocalAccessSpec
- Passed access from computeHostsAllowSpec
- Fixed pod for processTemplate()

* Sat Apr 07 2001 Gordon Rowell <gordonr@e-smith.com
- [1.5.0-06]
- Forward port patches between e-smith-lib-1.4.0-{06,11} (well, those which
  hadn't been back-ported)

* Tue Mar 27 2001 Peter Samuel <peters@e-smith.com>
- [1.5.0-05]
- syslog messages now cook % characters. Avoid sprintf errors.

* Fri Mar 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-04]
- event.pm now properly returns 1.

* Fri Mar 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-03]
- added optimized signal-event and event.pm

* Tue Mar 13 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Add computeNetmaskFromBits function
- Add l10N glue for Kirrily
- Add /etc/e-smith/templates-default directory containing
  default template-begin and template-end fragments, and stick
  that directory at the bottom of the template source stack.
- Fix expand-template so that it preserves ownership and mode.

* Tue Mar 13 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches upto 1.4.0-06.

* Fri Mar 02 2001 Tony Clayton <tonyc@e-smith.com>
- [1.4.0-06]
- esmith::config now ignores hash-comments/blank lines when reading hashes.

* Tue Feb 20 2001 Kirrily Robert <skud@e-smith.com>
- Added perldoc documentation (mostly just converted block comments)

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Fri Feb 02 2001 Tony Clayton <tonyc@e-smith.com>
- [1.4.0-03]
- Add sanity checks for variables passed to processTemplate

* Wed Jan 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-02]
- Change checking code for uid/gid so that we don't get warnings from
  attempts to set "root" as uid/gid.

* Mon Jan 29 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Roll new tarball which puts library back into .../5.005/esmith directory
  with compatibility symlink.

* Mon Jan 29 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-03]
- added preinstall logic to remove old esmith perl modules directory
  and symlink

* Thu Jan 25 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Fixed writable spec file.
- Remade tarball after moving esmith directory up a level

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-45.

* Wed Jan 24 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-45]
- Change all spellings adaptor=>adapter in ethernet.pm

* Wed Jan 24 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-44]
- BACKGROUND must be true (default) or false - otherwise complain

* Wed Jan 24 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-43]
- Added optional BACKGROUND=>(true|false) parameter to serviceControl
  This defaults to true, which runs start/stop/etc. in the background
  Set to false if the command should explictly be run in the foreground

* Tue Jan 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-42]
- Added dependency on Samba - required for password setting routines
- NOTE: Samba must currently be _installed_, but can be disabled

* Tue Jan 23 2001 Paul Nesbit <pkn@e-smith.com>
- [1.1.0-41]
- changed genSmallRedCell function in cgi.pm to use regular HTML instead
- of style sheet directives for created, italicized, red text.

* Fri Jan 12 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-39]
- added the ability to grab special editions from
  /home/e-smith/web/common/edition
  (used to be /etc/e-smith/web/common/edition in e-smith-base)

* Fri Jan 12 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-38]
- config.pm now correctly logs to syslog via /dev/log

* Fri Jan 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-37]
- If serviceControl() is given an InitscriptOrder, store it

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-36]
- ServiceOrder -> InitscriptOrder

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-35]
- Save/retrieve ServiceOrder in config db

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-34]
- Changed warning if no ORDER found, added graceful case

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-33]
- esmith::lib::serviceControl() complains if it can't work out the ORDER
  when it isn't provided

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-32]
- Log e-smith-bg output to syslog

* Thu Jan 11 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-31]
- Fixed line breaks in OLD config value logging

* Thu Jan 11 2001 Paul Nesbit <pkn@e-smith.com>
- [1.1.0-30]
- Fixed handling of system accounts in cgi.pm; now using db_get_type method,
  so system accounts w/ additional properties are not recognized on non-system
  accounts

* Wed Jan 10 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-29]
- Fixed config.pm log formatting for (undefined) values

* Wed Jan 10 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-28]
- Fixed all copyright notices

* Tue Jan  9 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-27]
- Avoid undefined value probs in log of config changes

* Mon Jan 8 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-26]
- config.pm now logs changes to STDERR. Eventually it will log to syslog.

* Mon Jan  8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-25]
- Handle missing file/directory in esmith::util::chownFile.

* Fri Jan  5 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-24]
- Make /sbin/e-smith/config just a wrapper for "db".

* Thu Jan  4 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-23]
- util.pm now conditionally generates a new LDAP password
  only if there isn't already one there.

* Tue Jan 2 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-22]
- ethernet.pm now gets kernel name from /proc/version instead of a
  call to uname(1).

* Thu Dec 21 2000 Paul Nesbit <pkn@e-smith.com>
- [1.1.0-21]
- Fixed cgi.pm to properly handle public telnet access warning

* Mon Dec 18 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-20]
- Moved processTemplate() documentation into function header and
  noted that we now merge templates-custom so you only need to put the
  modified/additional fragments into templates-custom

* Sun Dec 17 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-19]
- Fixed pattern match for RCS/SCCS/CVS
- serviceControl(... enable|disable ...) now both create the initscript
  symlink - service enable/disable is a property of the service. E.g. If we
  don't have the symlink for pppoe and enable pppoe in the bootstrap-console,
  it doesn't start since /etc/rc.d/rc will not have seen it when it
  builds its loop of rc scripts to run.

* Fri Dec 15 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-18]
- Skip over more bogus files in template directories, and skip
  over revision control directories if they exist.

* Thu Dec 14 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-17]
- Ignore *.rpmsave and *.rpmnew and *.rpmorig template fragments as
  they are leftover from an upgrade - probably pre template-custom
  vintage.

* Wed Dec 13 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-16]
- esmith::db::db_print forces db_get to return scalar value. This
  enables pipe chars to be printed.

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-15]
- Provide esmith::db to all template fragments

* Tue Dec 12 2000 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-14]
- fixed "dmfe" entry in pcitable.  Had an extra "Tab"

* Mon Dec 11 2000 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-13]
- fixed new bug in processTemplate

* Mon Dec 11 2000 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-12]
- updated the Davicom and a tulip nic driver
- renamed parameters in processTemplate, and provided usage examples

* Sun Dec 10 2000 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-11]
- bug fixes for FILE_PATH_LIST code

* Sun Dec 10 2000 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-10]
- Added muliple target files to processTemplate using FILE_PATH_LIST param
- Removed race condition and redundant renames in processTemplate

* Tue Dec 05 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-9]
- Removed dependency on kudzu

* Tue Dec 05 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-8]
- Chooses the newest of /usr/share/kudzu/pcitable or /etc/e-smith/pcitable
- Now has a dependency on kudzu.

* Thu Nov 30 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-7]
- Changed defined to scalar in db command for perl 5.6

* Wed Nov 22 2000 Peter Samuel <peters@e-smith.com>
- Changed ethernet.pm. It no longer has hard coded driver/card/chip
  details. It uses the output of lspci and compares that with
  /etc/e-smith/pcitable and the network modules in
  /lib/modules/`uname -r`/net.
- Added /etc/e-smith/pcitable. This is a copy of
  /usr/share/kudzu/pcitable from kudzu-0.72-3 from RH7.0

* Wed Nov 15 2000 Gordon Rowell <gordonr@e-smith.com>
- Changed if (defined %hash) test in util.pm to if (scalar%hash) for 5.6.0

* Wed Nov 15 2000 Tony Clayton <tonyc@e-smith.com>
- fixed bug in db.pm that required that hash members are always defined

* Wed Nov 15 2000 Gordon Rowell <gordonr@e-smith.com>
- Promoted site_perl/5.005/esmith to site_perl/esmith for perl-5.6.0
- Removed "defined" test in util.pm for perl-5.6.0

* Fri Nov 10 2000 Peter Samuel <peters@e-smith.com>
- Rolled version to 1.1.0-1. Includes patches up to 0.2-5.
- Fixed esmith/util.pm. Call to backgroundCommand in serviceControl
  had incorrect number of arguments.

* Sun Nov 05 2000 Charlie Brady <charlieb@e-smith.com>
- Allow null but defined type.

* Thu Nov 02 2000 Gordon Rowell <gordonr@e-smith.com>
- Modified util::computeLocalNetworkReversed() to align to the nearest byte
  boundary to the address/netmask combination

* Wed Nov 01 2000 Adrian Chung <achung@e-smith.com>
- Updated esmith::util::computeLocalNetworkShortSpec to use
  a hash for converting from dotted decimal quad notation
  to number of contiguous high order 'ones'.

* Tue Oct 31 2000 Charlie Brady <charlieb@e-smith.com>
- Change semantics of db_set to allow optional properties hash
- Change semantics of db_get to return type and properties list in
  array context.

* Thu Oct 26 2000 Peter Samuel <peters@e-smith.com>
- Rolled version to 0.2. Includes patches up to 0.1-33

* Thu Oct 19 2000 Adrian Chung <adrian.chung@e-smith.com>
- Update some code in cgi.pm to properly grab a value for TelnetServerMode

* Mon Oct 16 2000 Tony Clayton <tonyc@e-smith.com>
- reverted to Oct 06 functionality, since Text::Template won't report
  a meaningful line number upon throwing errors.  It looks as though we would
  need to modify Text::Template to make this happen.

* Thu Oct 12 2000 Tony Clayton <tonyc@e-smith.com>
- making sure temporary files are always unlinked.

* Thu Oct 12 2000 Tony Clayton <tonyc@e-smith.com>
- processTemplate now concatenates fragments and calls Text::Template once
  using a temporary file.

* Fri Oct 06 2000 Adrian Chung <adrian.chung@e-smith.com>
- Don't stop and start services in serviceControl{enable,disable}

* Thu Oct 05 2000 Adrian Chung <adrian.chung@e-smith.com>
- Unlink before attempting to symlink incase target already exists
  in serviceControl(enable).

* Thu Oct 05 2000 Peter Samuel <peters@e-smith.com>
- fixed db. DB_set was calling db_set_prop even if there were no
  properties to set. Fixed now.

* Thu Oct 05 2000 Gordon Rowell <gordonr@e-smith.com>
- Work out the serviceOrder if it wasn't provided to serviceControl()

* Thu Oct 05 2000 Peter Samuel <peters@e-smith.com>
- setdefault exits zeo if key exists - avoids possible problems in RPM %post
  actions

* Thu Oct 05 2000 Peter Samuel <peters@e-smith.com>
- Modified db. Now has a setdefault option that will set values only
  if the key does not exist.

* Thu Oct 05 2000 Gordon Rowell <gordonr@e-smith.com>
- Use backgroundCommand interface

* Thu Oct 05 2000 Gordon Rowell <gordonr@e-smith.com>
- Added start/stop/restart/reload to serviceControl() interface

* Tue Oct 03 2000 Charlie Brady <charlieb@e-smith.com>
- Do not expand templates if the destination already exists and
  is a directory.

* Tue Oct 03 2000 Charlie Brady <charlieb@e-smith.com>
- Change version number.

* Tue Oct 03 2000 Charlie Brady <charlieb@e-smith.com>
- Fix logical grouping error in code to only rename existing
  file if it already exists (in ProcessTemplate).

* Tue Oct 03 2000 Adrian Chung <achung@e-smith.com>
- Rebuilt on allspice

* Mon Sep 25 2000 Paul Nesbit <pkn@e-smith.com>
- replaced all references to .net with .com
- replaced all references to old phone number with new

* Fri Sep 22 2000 Charlie Brady <charlieb@e-smith.com>
- Allow undef values for group and user in chownFile

* Wed Sep 13 2000 Charlie Brady <charlieb@e-smith.com>
- Fix type mixups in default values in processTemplate
- Do chmod after file open - POSIX::open doesn't force
  file permissions.
- Expand template into temporary file, then rename.
- Only set UnsavedChanges flag in config if new value is different from
  old.

* Tue Sep 12 2000 Peter Samuel <peters@e-smith.com>
- Rewrote db_util.pm to be more generic.
- Renamed db_util.pm to db.pm
- Rewrote db to use the new db.pm and be more generic

* Fri Sep 1 2000 Tony Clayton <tony@e-smith.com>
- Fixed problem processing zero-length template fragments
- changed e-smith-devtools build requirement to >= 0.1-3

* Wed Aug 30 2000 Peter Samuel <peters@e-smith.com>
- Fixed db_util.pm. It now correctly handles e-smith
- config database format.

* Tue Aug 29 2000 Charlie Brady <charlieb@e-smith.com>
- Fix some problems in util.pm - can't use POSIX::open everywhere, and
  therefore shouldn't import it, and must use O_CREAT flag.
  Reformat and simplify processTemplate. Reformat to shiftwidth of 4.

* Mon Aug 28 2000 Tony Clayton <tony@e-smith.com>
- updated processTemplate function in util.pm to do in-order traversals of
  template source trees.  Now template directories can be deeper than one level.

* Mon Aug 28 2000 Tony Clayton <tony@e-smith.com>
- updated build dependency for devtools 1.0-2

* Fri Aug 25 2000 Charlie Brady <charlieb@e-smith.com>
- Added dependency on e-smith-devtools, and used genfilelist to
  make file list.

* Fri Aug 25 2000 Peter Samuel <peters@e-smith.com>
- Added a new perl module - db_util.pm
- Added a generic e-smith database utility - db

* Fri Aug 25 2000 Adrian Chung <mac@e-smith.com>
- Changed genHeader() in cgi.pm to read IMG SRC from environment variable
- ENV{'IMGHDR_SRC'} is now set in access.incl fragments per panel directory.

* Wed Aug 23 2000 Tony Clayton <tony@e-smith.com>
- Rewrote alot of processTemplate to take named parameters and process a list
of template sources of unknown size in sequence.
- Added perl-Text-Template dependency to spec file
- Release 4 and 5 are broken and are now deprecated

* Tue Aug 22 2000 Gordon Rowell <gordonr@e-smith.com>
- Modified serviceControl(...enable...) to use init.d/e-smith-service

* Tue Aug 22 2000 Gordon Rowell <gordonr@e-smith.com>
- Added serviceControl()

* Mon Aug 14 2000 Charlie Brady <charlieb@e-smith.net>
- Initial build

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

%pre
# Remove legacy symlink if one exists
[ -L /usr/lib/perl5/site_perl/esmith ] && rm -f /usr/lib/perl5/site_perl/esmith

# Move files from legacy dir if any exist
mkdir -p /usr/lib/perl5/site_perl/esmith
if [ -d /usr/lib/perl5/site_perl/5.005/esmith ]; then
    mv -f /usr/lib/perl5/site_perl/5.005/esmith/* \
    /usr/lib/perl5/site_perl/esmith
    rmdir /usr/lib/perl5/site_perl/5.005/esmith/
fi

#--------------------------------------------------
# add admin, public and www user accounts
#--------------------------------------------------
/usr/sbin/groupadd \
  -g 500 shared 2>/dev/null || :
/usr/sbin/useradd \
  -u 102 -c 'e-smith web server' -d /home/e-smith \
  -G shared -M -s /bin/false www 2>/dev/null || :
/usr/sbin/useradd \
  -u 101 -c 'e-smith administrator' -d /home/e-smith \
  -G shared,root,www -M -s /sbin/e-smith/console admin 2>/dev/null || :
/usr/sbin/useradd \
  -u 103 -c 'e-smith guest' -d /home/e-smith \
  -G shared -M -s /bin/false public 2>/dev/null || :
/usr/sbin/useradd \
  -u 1002 -c 'sme log user' -d /var/log/smelog \
  -M -s /bin/false smelog 2>/dev/null || :

exit 0

%post

%build
for event in post-install post-upgrade bootstrap-console-save console-save
do
    mkdir -p root/etc/e-smith/events/$event
done
perl createlinks
# build the test suite from embedded tests
/sbin/e-smith/buildtests 10e-smith-lib

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    | grep -v '/usr/lib/perl5/site_perl/esmith/Tai64n.pm' \
    >%{name}-%{version}-%{release}-filelist
echo "%doc Copying" >> %{name}-%{version}-%{release}-filelist
echo "%doc Artistic" >> %{name}-%{version}-%{release}-filelist
echo "%doc LICENSE" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%files Tai64n
%defattr(-,root,root)
%attr(0755,root,root) /usr/lib/perl5/site_perl/esmith/Tai64n.pm
