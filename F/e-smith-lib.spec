Summary: e-smith server and gateway - library module
%define name e-smith-lib
Name: %{name}
%define version 1.16.0
%define release 06
Version: %{version}
Release: %{release}
License: Artistic
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-lib-1.16.0-DBDeleteLog.patch
Patch1: e-smith-lib-1.16.0-NoSmbpasswdEnable.patch
Patch2: e-smith-lib-1.16.0-kudzu.patch
Patch3: e-smith-lib-1.16.0-templates.metadata.patch
Patch4: e-smith-lib-1.16.0-templates.metadata.patch2
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools >= 1.6.3-01
BuildRequires: e-smith-test >= 0.1.14
Obsoletes: %{name}-Tai64n
Requires: perl, perl(Text::Template)
Requires: perl(Time::HiRes), perl(MIME::Base64)
Requires: perl(Authen::PAM), perl(I18N::AcceptLanguage)
Requires: perl(I18N::LangTags) >= 0.27
Requires: perl(Net::IPv4Addr) >= 0.10

%description
e-smith server and gateway software - library module.

%changelog
* Mon Sep 25 2006 Charlie Brady <charlie_brady@mitel.com> 1.16.0-06
- Fix problem with greedy RE in template.metadata parsing. [SME: 1906]

* Fri Sep 08 2006 Charlie Brady <charlie_brady@mitel.com> 1.16.0-05
- Fix taint problem in template.metadata handling. [SME: 1906]

* Thu Apr 13 2006 Charlie Brady <charlie_brady@mitel.com> 1.16.0-04
- Use "kudzu --probe --class network" for NIC detection. [SME: 727]

* Fri Apr 7 2006 Gordon Rowell <gordonr@gormand.com.au> 1.16.0-03
- Don't call smbpasswd -e - setting the password is sufficient [SME: 1193]

* Tue Mar 28 2006 Gordon Rowell <gordonr@gormand.com.au> 1.16.0-02
- Log previous contents of db entry in DELETE log [SME: 1066]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.16.0-01
- Roll to stable stream version number. [SME: 1016]

* Fri Mar 10 2006 Charlie Brady <charlie_brady@mitel.com> 1.15.4-02
- Suppress warning from genSmallCell if text is undefined. [SME: 986]

* Fri Feb 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.15.4-01
- Roll patches up to 1.15.3-42
- Trim changelog prior to 1.15.0-01 [SME: 828]

* Thu Feb 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-42
- Adjust console title bar to 'SME Server' [SME: 726]

* Tue Feb 14 2006 Gordon Rowell <gordonr@gormand.com.au> 1.15.3-41
- Reworded text for template-begin and change URL to /development/
  rather than /custom/ [SME: 773]

* Mon Feb 13 2006 Charlie Brady <charlie_brady@mitel.com> 1.15.3-40
- Update URL in default template-begin fragment. [SME: 773]

* Sat Feb 11 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-39
- Remove obsolete e-smith-lib-Tai64n package. [SME: 689]

* Sat Feb 11 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-38
- [Null changelog for missing version - we accidentally skipped
   this version.]

* Sat Feb 11 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-37
- Fix get_all_by_prop in scalar context. [SME: 669,721]

* Mon Feb  6 2006 Shad L. Lords <slords@mail.com> 1.15.3-37
- Add ability to pass many props to get_all_by_prop [SME: 669]

* Mon Jan 23 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-36
- Fix warning during pseudonym deletion. [SME: 491]

* Fri Jan 20 2006 Charlie Brady <charlieb@e-smith.com> 1.15.3-35
- Fix up use of Sys::Syslog::syslog. [SME: 526]

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

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
    >%{name}-%{version}-%{release}-filelist
echo "%doc Copying" >> %{name}-%{version}-%{release}-filelist
echo "%doc Artistic" >> %{name}-%{version}-%{release}-filelist
echo "%doc LICENSE" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
