registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4368600912 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/jquery-1.4.2.min.js\np3\nsVtype\np4\nVtext/javascript\np5\ns.')
    _attrs_4368599184 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/ui-lightness/jquery-ui-1.8.6.custom.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4367351888 = _loads('(dp1\nVid\np2\nVtun-temperature\np3\ns.')
    _attrs_4368597584 = _loads('(dp1\nVid\np2\nVmain\np3\ns.')
    _attrs_4367352208 = _loads('(dp1\nVid\np2\nVtun-volume\np3\ns.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4368600656 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/custom-theme/jquery-ui.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4367558352 = _loads('(dp1\nVhref\np2\nVtun\np3\ns.')
    _attrs_4368600592 = _loads('(dp1\nVhref\np2\nV${request.application_url}/static/css/default.css\np3\nsVrel\np4\nVstylesheet\np5\nsVtype\np6\nVtext/css\np7\ns.')
    _attrs_4368599952 = _loads('(dp1\nVid\np2\nVside-bar\np3\ns.')
    _attrs_4367353168 = _loads('(dp1\n.')
    _attrs_4368598352 = _loads('(dp1\n.')
    _attrs_4368600720 = _loads('(dp1\nVtype\np2\nVtext/javascript\np3\ns.')
    _attrs_4368597456 = _loads('(dp1\nVid\np2\nVlineage\np3\ns.')
    _attrs_4368600336 = _loads('(dp1\n.')
    _attrs_4368598416 = _loads('(dp1\n.')
    _attrs_4367559248 = _loads('(dp1\n.')
    _attrs_4368598096 = _loads('(dp1\nVstyle\np2\nVwidth:400px;height:200px\np3\nsVclass\np4\nVanalog-history\np5\nsVid\np6\nVvolume-table\np7\ns.')
    _attrs_4367114960 = _loads('(dp1\n.')
    _attrs_4368599824 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/flot/jquery.flot.js\np3\nsVlanguage\np4\nVjavascript\np5\nsVtype\np6\nVtext/javascript\np7\ns.')
    _attrs_4366865360 = _loads('(dp1\nVhref\np2\nVhlt\np3\ns.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4368597328 = _loads('(dp1\nVstyle\np2\nVwidth:400px;height:200px\np3\nsVclass\np4\nVanalog-history\np5\nsVid\np6\nVtemperature-table\np7\ns.')
    _attrs_4368598608 = _loads('(dp1\n.')
    _attrs_4366868176 = _loads('(dp1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4366866320 = _loads('(dp1\n.')
    _attrs_4368598288 = _loads('(dp1\n.')
    _attrs_4368598160 = _loads('(dp1\n.')
    _attrs_4367115664 = _loads('(dp1\n.')
    _attrs_4368599312 = _loads('(dp1\nVsrc\np2\nV${request.application_url}/static/js/frontpage.js\np3\nsVtype\np4\nVtext/javascript\np5\ns.')
    _attrs_4367351952 = _loads('(dp1\nVhref\np2\nVboiler\np3\ns.')
    _attrs_4367355728 = _loads('(dp1\n.')
    _attrs_4367115152 = _loads('(dp1\nVid\np2\nVfermenter-temperature\np3\ns.')
    _attrs_4367117968 = _loads('(dp1\n.')
    _attrs_4367352144 = _loads('(dp1\n.')
    _attrs_4367352336 = _loads('(dp1\n.')
    _attrs_4367559056 = _loads('(dp1\n.')
    _attrs_4367117264 = _loads('(dp1\nVid\np2\nVboiler-temperature\np3\ns.')
    _attrs_4367116176 = _loads('(dp1\nVid\np2\nVboiler-volume\np3\ns.')
    _attrs_4367116304 = _loads('(dp1\n.')
    _attrs_4368427344 = _loads('(dp1\n.')
    _attrs_4366865680 = _loads('(dp1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _attrs_4367560208 = _loads('(dp1\n.')
    _attrs_4368598224 = _loads('(dp1\n.')
    _attrs_4367114640 = _loads('(dp1\n.')
    _attrs_4367117072 = _loads('(dp1\nVid\np2\nVfermenter-volume\np3\ns.')
    _attrs_4366865808 = _loads('(dp1\nVid\np2\nVhlt-temperature\np3\ns.')
    _attrs_4367117328 = _loads('(dp1\n.')
    _attrs_4368598736 = _loads('(dp1\n.')
    _attrs_4368598672 = _loads('(dp1\n.')
    _attrs_4366866640 = _loads('(dp1\n.')
    _attrs_4367352016 = _loads('(dp1\n.')
    _attrs_4366865488 = _loads('(dp1\nVid\np2\nVhlt-volume\np3\ns.')
    _attrs_4367114896 = _loads('(dp1\nVhref\np2\nVfermenter\np3\ns.')
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
        attrs = _attrs_4368598160
        _write(u'<html>\n  ')
        attrs = _attrs_4368598672
        _write(u'<head>\n    ')
        attrs = _attrs_4368599184
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
        attrs = _attrs_4368600592
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
        attrs = _attrs_4368600656
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
        attrs = _attrs_4368600912
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
        attrs = _attrs_4368599312
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
        attrs = _attrs_4368599824
        "join(value('request.application_url'), u'/static/js/flot/jquery.flot.js')"
        _write(u'<script language="javascript" type="text/javascript"')
        _tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/js/flot/jquery.flot.js', ))
        if (_tmp1 is _default):
            _tmp1 = u'${request.application_url}/static/js/flot/jquery.flot.js'
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
        attrs = _attrs_4368600720
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
        attrs = _attrs_4368598416
        _write(u'<body>\n    ')
        attrs = _attrs_4368598288
        _write(u'<header>\n      ')
        attrs = _attrs_4368597456
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
        attrs = _attrs_4368599952
        _write(u'<div id="side-bar">\n    </div>\n    ')
        attrs = _attrs_4368597584
        _write(u'<section id="main">\n      ')
        attrs = _attrs_4368597328
        _write(u'<div style="width:400px;height:200px" class="analog-history" id="temperature-table"></div>\n      ')
        attrs = _attrs_4368598096
        _write(u'<div style="width:400px;height:200px" class="analog-history" id="volume-table"></div>\n      ')
        attrs = _attrs_4368598224
        _write(u'<h1>Tanks</h1>\n      ')
        attrs = _attrs_4368600336
        _write(u'<table>\n        ')
        attrs = _attrs_4368598608
        _write(u'<tr>\n          ')
        attrs = _attrs_4368598352
        _write(u'<td>')
        attrs = _attrs_4366865360
        _write(u'<a href="hlt">Hot Liquor Tank</a></td>\n          ')
        attrs = _attrs_4368427344
        _write(u'<td>')
        attrs = _attrs_4366865808
        _write(u'<a id="hlt-temperature"></a>')
        attrs = _attrs_4366866640
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4366868176
        _write(u'<td>')
        attrs = _attrs_4366865488
        _write(u'<a id="hlt-volume"></a>')
        attrs = _attrs_4366866320
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4368598736
        _write(u'<tr>\n          ')
        attrs = _attrs_4367559056
        _write(u'<td>')
        attrs = _attrs_4367558352
        _write(u'<a href="tun">Mash/Lauder Tun</a></td>\n          ')
        attrs = _attrs_4367560208
        _write(u'<td>')
        attrs = _attrs_4367351888
        _write(u'<a id="tun-temperature"></a>')
        attrs = _attrs_4367353168
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4367559248
        _write(u'<td>')
        attrs = _attrs_4367352208
        _write(u'<a id="tun-volume"></a>')
        attrs = _attrs_4367352144
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4366865680
        _write(u'<tr>\n          ')
        attrs = _attrs_4367355728
        _write(u'<td>')
        attrs = _attrs_4367351952
        _write(u'<a href="boiler">Boiler</a></td>\n          ')
        attrs = _attrs_4367352336
        _write(u'<td>')
        attrs = _attrs_4367117264
        _write(u'<a id="boiler-temperature"></a>')
        attrs = _attrs_4367117968
        _write(u'<a> &deg;C</a></td>\n          ')
        attrs = _attrs_4367114960
        _write(u'<td>')
        attrs = _attrs_4367116176
        _write(u'<a id="boiler-volume"></a>')
        attrs = _attrs_4367117328
        _write(u'<a> L</a></td>\n        </tr>\n        ')
        attrs = _attrs_4367352016
        _write(u'<tr>\n          ')
        attrs = _attrs_4367114640
        _write(u'<td>')
        attrs = _attrs_4367114896
        _write(u'<a href="fermenter">Fermenter</a></td>\n          ')
        attrs = _attrs_4367116304
        _write(u'<td>')
        attrs = _attrs_4367115152
        _write(u'<a id="fermenter-temperature"></a></td>\n          ')
        attrs = _attrs_4367115664
        _write(u'<td>')
        attrs = _attrs_4367117072
        _write(u'<a id="fermenter-volume"></a></td>\n        </tr>\n      </table>\n    </section>\n  </body>\n</html>')
        return _out.getvalue()
    return render

__filename__ = u'/Users/craig/src/brewery/src/brewserver/brewserver/views/front_page_views/templates/front_page.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
