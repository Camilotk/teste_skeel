from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from pycpfcnpj import cpfcnpj
from .serializers import *
from .pagination import *

class CreateJobVacancy(APIView):
    def post(self, request):
        try:
            serializer = JobVacancySerializer(data=request.data)
            company_id = request.data['company']
            Company.objects.get(pk=company_id)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Company.DoesNotExist:
            return JsonResponse({"mensagem": "Empresa não registrada"},
                    status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro com skeel/views.py/CreateJobVacancy"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListJobVacancy(APIView):
    def post(self, request):
        try:
            jobs_list = JobVacancy.objects.all()
            paginator = VacancyPaginator()
            result_page = paginator.paginate_queryset(jobs_list, request)
            serializer = JobVacancySerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro com skeel/views.py/ListJobVacancy"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetJobByID(APIView):
    def post(self, request, pk):
        try:
            if pk <= "0":
                return JsonResponse({"mensagem": "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vacancy = JobVacancy.objects.get(pk=pk)
            serializer = JobVacancySerializer(vacancy)
            return Response(serializer.data)
        except JobVacancy.DoesNotExist:
            return JsonResponse({"mensagem": "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro com skeel/views.py/GetJobByID.post()"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditJobByID(APIView):
    def post(self, request, pk):
        try:
            if pk <= "0":
                return JsonResponse({"mensagem": "O ID deve ser maior que zero."},
                        status=status.HTTP_400_BAD_REQUEST)
            vacancy = JobVacancy.objects.get(pk=pk)
            serializer = JobVacancySerializer(vacancy, data=request.data)
            company_id = request.data["company"]
            Company.objects.get(pk=company_id)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        except JobVacancy.DoesNotExist:
            return JsonResponse({"mensagem": "Isso non ecziste!"},
                    status=status.HTTP_404_NOT_FOUND)
        except Company.DoesNotExist:
            return JsonResponse({"mensagem": "A companhia da relação não existe"},
                    status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro com skeel/views.py/GetJobByID.put())"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteJobByID(APIView):
    def post(self, request, pk):
        try:
            if pk <= "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                        status=status.HTTP_400_BAD_REQUEST)
            vacancy = JobVacancy.objects.get(pk=pk)
            vacancy.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                    status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateCompany(APIView):
    def post(self, request):
        try:
            serializer = CompanySerializer(data=request.data)
            cnpj = request.data['cnpj']
            if cpfcnpj.validate(cnpj) and serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro no servidor"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListCompany(APIView):
    def post(self, request):
        try:
            company_list = Company.objects.all()
            paginator = CompanyPaginator()
            result_page = paginator.paginate_queryset(company_list, request)
            serializer = CompanySerializer(company_list, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro em skeel/views.py/CompanyList"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetCompanyByID(APIView):
    def post(self, request, pk):
        try:
            if pk <= "0":
                return JsonResponse({"mensagem": "O ID tem que ser maior que 0"},
                        status=status.HTTP_400_BAD_REQUEST)
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return JsonResponse({"mensagem": "Empresa não existe"},
                    status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro em skeel/views.py/GetCompanyByID"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditCompanyByID(APIView):
    def post(self, request, pk):
        try:
            if pk <= "0":
                return JsonResponse({"mensagem": "O ID tem que ser maior que 0"},
                        status=status.HTTP_400_BAD_REQUEST)
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company, data=request.data)
            cnpj = request.data['cnpj']
            if cpfcnpj.validate(cnpj) and serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Company.DoesNotExist:
            return JsonResponse({"mensagem": "A empresa não existe"},
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({"mensagem": "Ocorreu um erro em skeel/views.py/EditCompanyByID"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteCompanyByID(APIView):
    def post(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                        status=status.HTTP_400_BAD_REQUEST)
            company = Company.objects.get(pk = pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Company.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa não existe"},
                    status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
