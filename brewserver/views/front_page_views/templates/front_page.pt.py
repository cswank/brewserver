registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _attrs_4372744656 = _loads('(dp1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4365808400 = _loads('(dp1\n.')
    _attrs_4365810512 = _loads('(dp1\n.')
    _attrs_4365808912 = _loads('(dp1\n.')
    _attrs_4365808528 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4365808208 = _loads('(dp1\nVid\np2\nVtun-volume\np3\ns.')
    _attrs_4365807952 = _loads('(dp1\n.')
    _attrs_4365811600 = _loads('(dp1\nVid\np2\nVboiler-volume\np3\ns.')
    _attrs_4365977424 = _loads('(dp1\n.')
    _attrs_4365932304 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/custom-theme/jquery-ui.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4365807824 = _loads('(dp1\nVhref\np2\nVboiler\np3\ns.')
    _attrs_4365932560 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/frontpage.js\np3\nsVtype\np4\nVtext/javascript\np5\ns.')
    _attrs_4365932752 = _loads('(dp1\n.')
    _attrs_4365976720 = _loads('(dp1\n.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4372745424 = _loads('(dp1\n.')
    _attrs_4365930768 = _loads('(dp1\nVtype\np2\nVtext/javascript\np3\ns.')
    _attrs_4365808080 = _loads('(dp1\n.')
    _attrs_4365903632 = _loads('(dp1\n.')
    _attrs_4365810960 = _loads('(dp1\nVhref\np2\nVtun\np3\ns.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4365977744 = _loads('(dp1\n.')
    _attrs_4372745936 = _loads('(dp1\n.')
    _attrs_4365931280 = _loads('(dp1\nVid\np2\nVmain-content\np3\ns.')
    _attrs_4365979088 = _loads('(dp1\n.')
    _attrs_4365932240 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/default.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4365976272 = _loads('(dp1\n.')
    _attrs_4365976336 = _loads('(dp1\nVhref\np2\nVhlt\np3\ns.')
    _attrs_4372746064 = _loads('(dp1\nVid\np2\nVfermenter-temperature\np3\ns.')
    _attrs_4365978512 = _loads('(dp1\n.')
    _attrs_4365932432 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/jquery-1.4.2.min.js\np3\nsVtype\np4\nVtext/javascript\np5\ns.')
    _attrs_4365932368 = _loads('(dp1\n.')
    _attrs_4372745104 = _loads('(dp1\nVhref\np2\nVfermenter\np3\ns.')
    _attrs_4365811344 = _loads('(dp1\n.')
    _attrs_4365808848 = _loads('(dp1\nVid\np2\nVboiler-temperature\np3\ns.')
    _attrs_4365976080 = _loads('(dp1\nVid\np2\nVhlt-volume\np3\ns.')
    _attrs_4365971600 = _loads('(dp1\nVid\np2\nVfermenter-volume\np3\ns.')
    _attrs_4365977552 = _loads('(dp1\n.')
    _attrs_4365902352 = _loads('(dp1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _attrs_4365931600 = _loads('(dp1\nVid\np2\nVside-bar\np3\ns.')
    _attrs_4365932176 = _loads('(dp1\nVid\np2\nVheader\np3\ns.')
    _attrs_4365904208 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/ui-lightness/jquery-ui-1.8.6.custom.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4365808784 = _loads('(dp1\n.')
    _attrs_4365979024 = _loads('(dp1\n.')
    _attrs_4365808592 = _loads('(dp1\nVid\np2\nVtun-temperature\np3\ns.')
    _attrs_4365978256 = _loads('(dp1\nVid\np2\nVhlt-temperature\np3\ns.')
    _attrs_4365978128 = _loads('(dp1\n.')
    _attrs_4365809168 = _loads('(dp1\n.')
    _attrs_4365808336 = _loads('(dp1\n.')
    _attrs_4365931408 = _loads('(dp1\nVid\np2\nVlineage\np3\ns.')
    _attrs_4365807696 = _loads('(dp1\n.')
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
        attrs = _attrs_4365902352
        _write(u'<html>\n  ')
        attrs = _attrs_4365903632
        _write(u'<head>\n    ')
        attrs = _attrs_4365904208
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
        attrs = _attrs_4365932240
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
        attrs = _attrs_4365932304
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
        attrs = _attrs_4365932432
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
        attrs = _attrs_4365932560
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
        attrs = _attrs_4365930768
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
        attrs = _attrs_4365932368
        _write(u'<body>\n    ')
        attrs = _attrs_4365932176
        _write(u'<div id="header">\n      ')
        attrs = _attrs_4365931408
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
        _write(u'</div>\n    </div>\n    ')
        attrs = _attrs_4365931600
        _write(u'<div id="side-bar">\n    </div>\n    ')
        attrs = _attrs_4365931280
        _write(u'<div id="main-content">\n      ')
        attrs = _attrs_4365932752
        _write(u'<h1>Tanks</h1>\n      ')
        attrs = _attrs_4365979024
        _write(u'<table>\n        ')
        attrs = _attrs_4365979088
        _write(u'<tr>\n          ')
        attrs = _attrs_4365978128
        _write(u'<td>')
        attrs = _attrs_4365976336
        _write(u'<a href="hlt">Hot Liquor Tank</a></td>\n          ')
        attrs = _attrs_4365977424
        _write(u'<td>')
        attrs = _attrs_4365978256
        _write(u'<a id="hlt-temperature"></a>')
        attrs = _attrs_4365978512
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4365977744
        _write(u'<td>')
        attrs = _attrs_4365976080
        _write(u'<a id="hlt-volume"></a>')
        attrs = _attrs_4365976720
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4365977552
        _write(u'<tr>\n          ')
        attrs = _attrs_4365976272
        _write(u'<td>')
        attrs = _attrs_4365810960
        _write(u'<a href="tun">Mash/Lauder Tun</a></td>\n          ')
        attrs = _attrs_4365807696
        _write(u'<td>')
        attrs = _attrs_4365808592
        _write(u'<a id="tun-temperature"></a>')
        attrs = _attrs_4365811344
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4365808912
        _write(u'<td>')
        attrs = _attrs_4365808208
        _write(u'<a id="tun-volume"></a>')
        attrs = _attrs_4365808528
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4365810512
        _write(u'<tr>\n          ')
        attrs = _attrs_4365808336
        _write(u'<td>')
        attrs = _attrs_4365807824
        _write(u'<a href="boiler">Boiler</a></td>\n          ')
        attrs = _attrs_4365808784
        _write(u'<td>')
        attrs = _attrs_4365808848
        _write(u'<a id="boiler-temperature"></a>')
        attrs = _attrs_4365808400
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4365809168
        _write(u'<td>')
        attrs = _attrs_4365811600
        _write(u'<a id="boiler-volume"></a>')
        attrs = _attrs_4365807952
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4365808080
        _write(u'<tr>\n          ')
        attrs = _attrs_4372745936
        _write(u'<td>')
        attrs = _attrs_4372745104
        _write(u'<a href="fermenter">Fermenter</a></td>\n          ')
        attrs = _attrs_4372744656
        _write(u'<td>')
        attrs = _attrs_4372746064
        _write(u'<a id="fermenter-temperature"></a></td>\n          ')
        attrs = _attrs_4372745424
        _write(u'<td>')
        attrs = _attrs_4365971600
        _write(u'<a id="fermenter-volume"></a></td>\n        </tr>\n      </table>\n    </div>\n  </body>\n</html>')
        return _out.getvalue()
    return render

__filename__ = u'/Users/cswank/.virtualenvs/brewery/src/brewserver/brewserver/views/front_page_views/templates/front_page.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
