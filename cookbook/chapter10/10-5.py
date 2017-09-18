# 공통된 네임스페이스에 코드 임포트 디렉터리 만들기

import sys
sys.path.extend(['cookbook.test', 'cookbook.test2'])
import spam.blah
import spam.grok

