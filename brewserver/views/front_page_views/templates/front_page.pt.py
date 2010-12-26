registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _attrs_4352392528 = _loads('(dp1\nVid\np2\nVtun-volume\np3\ns.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4365149584 = _loads('(dp1\n.')
    _attrs_4352391376 = _loads('(dp1\n.')
    _attrs_4352392400 = _loads('(dp1\n.')
    _attrs_4365151056 = _loads('(dp1\n.')
    _attrs_4365897360 = _loads('(dp1\nVid\np2\nVmain\np3\ns.')
    _attrs_4365267984 = _loads('(dp1\n.')
    _attrs_4365137936 = _loads('(dp1\nVid\np2\nVfermenter-volume\np3\ns.')
    _attrs_4365118032 = _loads('(dp1\nVid\np2\nVhlt-volume\np3\ns.')
    _attrs_4365160912 = _loads('(dp1\nVid\np2\nVboiler-temperature\np3\ns.')
    _attrs_4365267536 = _loads('(dp1\n.')
    _attrs_4352392464 = _loads('(dp1\n.')
    _attrs_4365162704 = _loads('(dp1\n.')
    _attrs_4365117776 = _loads('(dp1\n.')
    _attrs_4365150160 = _loads('(dp1\nVhref\np2\nVhlt\np3\ns.')
    _attrs_4365267600 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/custom-theme/jquery-ui.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4365267216 = _loads('(dp1\n.')
    _attrs_4365150352 = _loads('(dp1\n.')
    _attrs_4352391760 = _loads('(dp1\n.')
    _attrs_4365267024 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/default.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4365118800 = _loads('(dp1\n.')
    _attrs_4365118544 = _loads('(dp1\nVhref\np2\nVtun\np3\ns.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4365151440 = _loads('(dp1\nVid\np2\nVhlt-temperature\np3\ns.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4352391504 = _loads('(dp1\nVid\np2\nVtun-temperature\np3\ns.')
    _attrs_4365894480 = _loads('(dp1\nVid\np2\nVside-bar\np3\ns.')
    _attrs_4365893904 = _loads('(dp1\nVid\np2\nVlineage\np3\ns.')
    _attrs_4365116048 = _loads('(dp1\n.')
    _attrs_4365160976 = _loads('(dp1\nVid\np2\nVboiler-volume\np3\ns.')
    _attrs_4365160528 = _loads('(dp1\n.')
    _attrs_4352392720 = _loads('(dp1\nVhref\np2\nVboiler\np3\ns.')
    _attrs_4365162896 = _loads('(dp1\n.')
    _attrs_4352392144 = _loads('(dp1\n.')
    _attrs_4365895952 = _loads('(dp1\nVtype\np2\nVtext/javascript\np3\ns.')
    _attrs_4365151888 = _loads('(dp1\n.')
    _attrs_4365161232 = _loads('(dp1\nVhref\np2\nVfermenter\np3\ns.')
    _attrs_4365152016 = _loads('(dp1\n.')
    _attrs_4352392656 = _loads('(dp1\n.')
    _attrs_4365149328 = _loads('(dp1\n.')
    _attrs_4365149776 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _attrs_4365894992 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/jquery-1.4.2.min.js\np3\nsVtype\np4\nVtext/javascript\np5\ns.')
    _attrs_4365135952 = _loads('(dp1\nVid\np2\nVfermenter-temperature\np3\ns.')
    _attrs_4352392848 = _loads('(dp1\n.')
    _attrs_4365267792 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/ui-lightness/jquery-ui-1.8.6.custom.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4365116944 = _loads('(dp1\n.')
    _attrs_4365894800 = _loads('(dp1\n.')
    _attrs_4365895504 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/frontpage.js\np3\nsVtype\np4\nVtext/javascript\np5\ns.')
    _attrs_4365163472 = _loads('(dp1\n.')
    _attrs_4365162064 = _loads('(dp1\n.')
    _attrs_4365897296 = _loads('(dp1\n.')
    def render(econtext, rcontext=None):
        macros = econtext.get('macros')
        _translate = econtext.get('_translate')
        _slots = econtext.get('_slots')
        target_language = econtext.get('target_language')
        u'_init_stream()'
        (_out, _write, ) = _init_stream()
        u'_init_tal()'
        (_attributes, repeat, ) = _init_tal()
        u'_init_default()'
        _default = _init_default()
        u'None'
        default = None
        u'None'
        _domain = None
        attrs = _attrs_4365267984
        _write(u'<html>\n  ')
        attrs = _attrs_4365267536
        _write(u'<head>\n    ')
        attrs = _attrs_4365267792
        "join(value('request.application_url'), u'/static/css/ui-lightness/jquery-ui-1.8.6.custom.css')"
        _write(u'<link')
        _tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/css/ui-lightness/jquery-ui-1.8.6.custom.css', ))
        if (_tmp1 is _default):
            _tmp1 = u'${request.application_url}/static/css/ui-lightness/jquery-ui-1.8.6.custom.css'
        if ((_tmp1 is not None) and (_tmp1 is not False)):
            if (_tmp1.__class__ not in (str, unicode, int, float, )):
                _tmp1 = unicode(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
            else:
                if not isinstance(_tmp1, unicode):
                    _tmp1 = str(_tmp1)
            if ('&' in _tmp1):
                if (';' in _tmp1):
                    _tmp1 = _re_amp.sub('&amp;', _tmp1)
                else:
                    _tmp1 = _tmp1.replace('&', '&amp;')
            if ('<' in _tmp1):
                _tmp1 = _tmp1.replace('<', '&lt;')
            if ('>' in _tmp1):
                _tmp1 = _tmp1.replace('>', '&gt;')
            if ('"' in _tmp1):
                _tmp1 = _tmp1.replace('"', '&quot;')
            _write(((' href="' + _tmp1) + '"'))
        _write(u' rel="stylesheet" type="text/css" />\n    ')
        attrs = _attrs_4365267024
        _write(u'<link')
        default = u'${request.application_url}/static/css/default.css'
        "join(value('request.application_url'), u'/static/css/default.css')"
        _tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/css/default.css', ))
        default = None
        if (_tmp1 is _default):
            _tmp1 = u'${request.application_url}/static/css/default.css'
        if ((_tmp1 is not None) and (_tmp1 is not False)):
            if (_tmp1.__class__ not in (str, unicode, int, float, )):
                _tmp1 = unicode(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
            else:
                if not isinstance(_tmp1, unicode):
                    _tmp1 = str(_tmp1)
            if ('&' in _tmp1):
                if (';' in _tmp1):
                    _tmp1 = _re_amp.sub('&amp;', _tmp1)
                else:
                    _tmp1 = _tmp1.replace('&', '&amp;')
            if ('<' in _tmp1):
                _tmp1 = _tmp1.replace('<', '&lt;')
            if ('>' in _tmp1):
                _tmp1 = _tmp1.replace('>', '&gt;')
            if ('"' in _tmp1):
                _tmp1 = _tmp1.replace('"', '&quot;')
            _write(((' href="' + _tmp1) + '"'))
        _write(u' rel="stylesheet" type="text/css" />\n    ')
        attrs = _attrs_4365267600
        "join(value('request.application_url'), u'/static/css/custom-theme/jquery-ui.css')"
        _write(u'<link')
        _tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/css/custom-theme/jquery-ui.css', ))
        if (_tmp1 is _default):
            _tmp1 = u'${request.application_url}/static/css/custom-theme/jquery-ui.css'
        if ((_tmp1 is not None) and (_tmp1 is not False)):
            if (_tmp1.__class__ not in (str, unicode, int, float, )):
                _tmp1 = unicode(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
            else:
                if not isinstance(_tmp1, unicode):
                    _tmp1 = str(_tmp1)
            if ('&' in _tmp1):
                if (';' in _tmp1):
                    _tmp1 = _re_amp.sub('&amp;', _tmp1)
                else:
                    _tmp1 = _tmp1.replace('&', '&amp;')
            if ('<' in _tmp1):
                _tmp1 = _tmp1.replace('<', '&lt;')
            if ('>' in _tmp1):
                _tmp1 = _tmp1.replace('>', '&gt;')
            if ('"' in _tmp1):
                _tmp1 = _tmp1.replace('"', '&quot;')
            _write(((' href="' + _tmp1) + '"'))
        _write(u' rel="stylesheet" type="text/css" />\n    ')
        attrs = _attrs_4365894992
        "join(value('request.application_url'), u'/static/js/jquery-1.4.2.min.js')"
        _write(u'<script type="text/javascript"')
        _tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/js/jquery-1.4.2.min.js', ))
        if (_tmp1 is _default):
            _tmp1 = u'${request.application_url}/static/js/jquery-1.4.2.min.js'
        if ((_tmp1 is not None) and (_tmp1 is not False)):
            if (_tmp1.__class__ not in (str, unicode, int, float, )):
                _tmp1 = unicode(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
            else:
                if not isinstance(_tmp1, unicode):
                    _tmp1 = str(_tmp1)
            if ('&' in _tmp1):
                if (';' in _tmp1):
                    _tmp1 = _re_amp.sub('&amp;', _tmp1)
                else:
                    _tmp1 = _tmp1.replace('&', '&amp;')
            if ('<' in _tmp1):
                _tmp1 = _tmp1.replace('<', '&lt;')
            if ('>' in _tmp1):
                _tmp1 = _tmp1.replace('>', '&gt;')
            if ('"' in _tmp1):
                _tmp1 = _tmp1.replace('"', '&quot;')
            _write(((' src="' + _tmp1) + '"'))
        _write(u'></script>\n    ')
        attrs = _attrs_4365895504
        "join(value('request.application_url'), u'/static/js/frontpage.js')"
        _write(u'<script type="text/javascript"')
        _tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/js/frontpage.js', ))
        if (_tmp1 is _default):
            _tmp1 = u'${request.application_url}/static/js/frontpage.js'
        if ((_tmp1 is not None) and (_tmp1 is not False)):
            if (_tmp1.__class__ not in (str, unicode, int, float, )):
                _tmp1 = unicode(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
            else:
                if not isinstance(_tmp1, unicode):
                    _tmp1 = str(_tmp1)
            if ('&' in _tmp1):
                if (';' in _tmp1):
                    _tmp1 = _re_amp.sub('&amp;', _tmp1)
                else:
                    _tmp1 = _tmp1.replace('&', '&amp;')
            if ('<' in _tmp1):
                _tmp1 = _tmp1.replace('<', '&lt;')
            if ('>' in _tmp1):
                _tmp1 = _tmp1.replace('>', '&gt;')
            if ('"' in _tmp1):
                _tmp1 = _tmp1.replace('"', '&quot;')
            _write(((' src="' + _tmp1) + '"'))
        _write(u'></script>\n    ')
        attrs = _attrs_4365895952
        u'state_url'
        _write(u'<script type="text/javascript">\n      var stateUrl = "')
        _tmp1 = econtext['state_url']
        _tmp = _tmp1
        if (_tmp.__class__ not in (str, unicode, int, float, )):
            try:
                _tmp = _tmp.__html__
            except:
                _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
            else:
                _tmp = _tmp()
                _write(_tmp)
                _tmp = None
        if (_tmp is not None):
            if not isinstance(_tmp, unicode):
                _tmp = str(_tmp)
            if ('&' in _tmp):
                if (';' in _tmp):
                    _tmp = _re_amp.sub('&amp;', _tmp)
                else:
                    _tmp = _tmp.replace('&', '&amp;')
            if ('<' in _tmp):
                _tmp = _tmp.replace('<', '&lt;')
            if ('>' in _tmp):
                _tmp = _tmp.replace('>', '&gt;')
            _write(_tmp)
        _write(u'";\n    </script>\n  </head>\n  ')
        attrs = _attrs_4365267216
        _write(u'<body>\n    ')
        attrs = _attrs_4365897296
        _write(u'<header>\n      ')
        attrs = _attrs_4365893904
        u"''"
        _write(u'<div id="lineage">')
        _default.value = default = ''
        u'lineage'
        _content = econtext['lineage']
        u'_content'
        _tmp1 = _content
        _tmp = _tmp1
        if (_tmp.__class__ not in (str, unicode, int, float, )):
            try:
                _tmp = _tmp.__html__
            except:
                _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
            else:
                _tmp = _tmp()
                _write(_tmp)
                _tmp = None
        if (_tmp is not None):
            if not isinstance(_tmp, unicode):
                _tmp = str(_tmp)
            _write(_tmp)
        _write(u'</div>\n    </header>\n    ')
        attrs = _attrs_4365894480
        _write(u'<div id="side-bar">\n    </div>\n    ')
        attrs = _attrs_4365897360
        _write(u'<section id="main">\n      ')
        attrs = _attrs_4365894800
        _write(u'<h1>Tanks</h1>\n      ')
        attrs = _attrs_4365151056
        _write(u'<table>\n        ')
        attrs = _attrs_4365152016
        _write(u'<tr>\n          ')
        attrs = _attrs_4365150352
        _write(u'<td>')
        attrs = _attrs_4365150160
        _write(u'<a href="hlt">Hot Liquor Tank</a></td>\n          ')
        attrs = _attrs_4365149776
        _write(u'<td>')
        attrs = _attrs_4365151440
        _write(u'<a id="hlt-temperature"></a>')
        attrs = _attrs_4365149328
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4365151888
        _write(u'<td>')
        attrs = _attrs_4365118032
        _write(u'<a id="hlt-volume"></a>')
        attrs = _attrs_4365118800
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4365149584
        _write(u'<tr>\n          ')
        attrs = _attrs_4365116944
        _write(u'<td>')
        attrs = _attrs_4365118544
        _write(u'<a href="tun">Mash/Lauder Tun</a></td>\n          ')
        attrs = _attrs_4365116048
        _write(u'<td>')
        attrs = _attrs_4352391504
        _write(u'<a id="tun-temperature"></a>')
        attrs = _attrs_4352392656
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4352391376
        _write(u'<td>')
        attrs = _attrs_4352392528
        _write(u'<a id="tun-volume"></a>')
        attrs = _attrs_4352391760
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4365117776
        _write(u'<tr>\n          ')
        attrs = _attrs_4352392848
        _write(u'<td>')
        attrs = _attrs_4352392720
        _write(u'<a href="boiler">Boiler</a></td>\n          ')
        attrs = _attrs_4352392464
        _write(u'<td>')
        attrs = _attrs_4365160912
        _write(u'<a id="boiler-temperature"></a>')
        attrs = _attrs_4365162896
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4352392144
        _write(u'<td>')
        attrs = _attrs_4365160976
        _write(u'<a id="boiler-volume"></a>')
        attrs = _attrs_4365163472
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4352392400
        _write(u'<tr>\n          ')
        attrs = _attrs_4365160528
        _write(u'<td>')
        attrs = _attrs_4365161232
        _write(u'<a href="fermenter">Fermenter</a></td>\n          ')
        attrs = _attrs_4365162064
        _write(u'<td>')
        attrs = _attrs_4365135952
        _write(u'<a id="fermenter-temperature"></a></td>\n          ')
        attrs = _attrs_4365162704
        _write(u'<td>')
        attrs = _attrs_4365137936
        _write(u'<a id="fermenter-volume"></a></td>\n        </tr>\n      </table>\n    </section>\n  </body>\n</html>')
        return _out.getvalue()
    return render

__filename__ = u'/Users/craig/src/brewery/src/brewserver/brewserver/views/front_page_views/templates/front_page.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
