import imp
from django.shortcuts import render
import subprocess , json
from django.http import JsonResponse


def ping_test(request):
	result = subprocess.Popen(['ansible-playbook', 'vm.yml', '--extra-vars' ], stdout=subprocess.PIPE)
	output, err = result.communicate()
	return JsonResponse(json.loads(output))