VERSION=1
TMPDIR=temp
RELEASE=itunes-refresh-$(VERSION)
RELDIR=$(TMPDIR)/$(RELEASE)

release:
	rm -rf $(RELDIR)
	mkdir -p $(RELDIR)/bin
	mkdir -p $(RELDIR)/src/Properties
	cp -p *.txt $(RELDIR)
	cp -p itunes-refresh.cs $(RELDIR)/src
	cp -p itunes-refresh.csproj $(RELDIR)/src
	cp -p itunes-refresh.sln $(RELDIR)/src
	cp -p Properties/AssemblyInfo.cs $(RELDIR)/src/Properties
	cp -p bin/Release/itunes-refresh.exe $(RELDIR)/bin
	cp -p bin/Release/Interop.iTunesLib.dll $(RELDIR)/bin
	cd $(TMPDIR) && zip -r $(RELEASE).zip $(RELEASE)
	@echo ""
	@echo Build complete, see $(TMPDIR)/$(RELEASE).zip
