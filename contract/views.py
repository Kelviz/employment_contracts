import logging
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token
from rest_framework import serializers, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import EmploymentAgreement
from .serializers import UserSerializer, EmploymentAgreementSerializers, LoginSerializer
from datetime import datetime
from django.db import transaction


logger = logging.getLogger(__name__)

@swagger_auto_schema(
    operation_description="List and Create an employment agreement",
    responses={200: EmploymentAgreementSerializers}
)

class EmploymentAgreementListCreate(generics.ListCreateAPIView):
        #List And Create Employment Agreement view
        queryset = EmploymentAgreement.objects.all()
        serializer_class = EmploymentAgreementSerializers

        def get(request, *args,  **kwargs):
                logger.info("Listing All Employment Agreements")
                try:
                        return super().get(request, *args, **kwargs)
                except Exception as e:
                        logger.error(f"Error Listing Employment Agreements {e}")
                        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
                
        def post(self, request, *args, **kwargs):
                logger.info("Creating A New Employment Agreement.")
                logger.debug(f"Request Data: {request.data}")

                #Return 400 Bad Request if the fields are empty
                serializer = EmploymentAgreementSerializers(data=request.data)
                if not serializer.is_valid():
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
                              
                #Check for empty fields
                empty_fields = [field for field, value in request.data.items() if value in [None, '', []]]
                if empty_fields:
                        error_message = f"Empty fields found: {', '.join(empty_fields)}"
                        logger.error(error_message)
                        return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
                 
                #Check for negative salary
                salary = request.data.get('salary')
                if salary is not None and float(salary) < 0:
                        error_message = "Salary cannot be negative"
                        logger.error(error_message)
                        return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

                try:
                      return super().post(request, *args, **kwargs)               
                except Exception as e:
                        logger.error(f"Error Creating Employment Agreements {e}")
                        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
                


class EmploymentAgreementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = EmploymentAgreement.objects.all()
        serializer_class = EmploymentAgreementSerializers

        def get_object(self, pk):
                try:
                        return EmploymentAgreement.objects.get(pk=pk)
                except EmploymentAgreement.DoesNotExist:
                        raise NotFound(detail="Employment agreement not found")

        def get(self, request, *args, **kwargs):
                logger.info(f"Retrieving employment agreement with ID: {kwargs.get('pk')}")
                try:
                        instance = self.get_object(kwargs.get('pk'))
                        serializer = self.get_serializer(instance)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                except NotFound as e:
                        logger.warning(f"Employment agreement with ID {kwargs.get('pk')} not found: {str(e)}")
                        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                        logger.error(f"Error retrieving employment agreement: {e}")
                        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

        def put(self, request, *args, **kwargs):
                logger.info(f"Updating employment agreement with ID: {kwargs.get('pk')}")
                logger.debug(f"Request Data: {request.data}")

                try:
                        response = super().put(request, *args, **kwargs)
                        return response              
                except Exception as e:
                        logger.error(f"Error updating employment agreement: {e}")
                        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

        def delete(self, request, *args, **kwargs):
                logger.info(f"Deleting employment agreement with ID: {kwargs.get('pk')}")
                try:
                        response = super().delete(request, *args, **kwargs)
                        return Response({"success": "Employment agreement deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
                except Exception as e:
                        logger.error("Error deleting employment agreement: {e}")
                        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                


class EmploymentAgreementSearch(generics.ListAPIView):
    queryset = EmploymentAgreement.objects.all()
    serializer_class = EmploymentAgreementSerializers
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('employee_name', openapi.IN_QUERY, description="Employee name", type=openapi.TYPE_STRING),
            openapi.Parameter('role', openapi.IN_QUERY, description="Role", type=openapi.TYPE_STRING),
            openapi.Parameter('salary_min', openapi.IN_QUERY, description="Minimum salary", type=openapi.TYPE_NUMBER),
            openapi.Parameter('salary_max', openapi.IN_QUERY, description="Maximum salary", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Start date (YYYY-MM-DD)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="End date (YYYY-MM-DD)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        ]
    )
    def get(self, request, *args, **kwargs):
        logger.info("Searching employment agreements")
        
        try:
            queryset = self.get_queryset()

            # Get search parameters
            employee_name = self.request.query_params.get('employee_name', None)
            role = self.request.query_params.get('role', None)
            salary_min = self.request.query_params.get('salary_min', None)
            salary_max = self.request.query_params.get('salary_max', None)
            start_date = self.request.query_params.get('start_date', None)
            end_date = self.request.query_params.get('end_date', None)

            # Filter queryset based on parameters
            if employee_name is not None:
                queryset = queryset.filter(employee_name__icontains=employee_name)
            if role is not None:
                queryset = queryset.filter(role__icontains=role)
            if salary_min is not None:
                queryset = queryset.filter(salary__gte=salary_min)
            if salary_max is not None:
                queryset = queryset.filter(salary__lte=salary_max)
            if start_date is not None:
                try:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d')
                    queryset = queryset.filter(start_date__gte=start_date)
                except ValueError:
                    raise serializers.ValidationError({"start_date": "Incorrect date format, should be YYYY-MM-DD"})
            if end_date is not None:
                try:
                    end_date = datetime.strptime(end_date, '%Y-%m-%d')
                    queryset = queryset.filter(end_date__lte=end_date)
                except ValueError:
                    raise serializers.ValidationError({"end_date": "Incorrect date format, should be YYYY-MM-DD"})

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Error searching employment agreements")
            return Response({"error":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SignupView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
            },
            required=['username', 'password', 'email']
        ),
    )


    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            logger.info(f"Creating new user: {request.data['username']}")
            try:
                with transaction.atomic():
                    user = serializer.save()
                    token = Token.objects.create(user=user)
                    logger.info(f"User created successfully: {user.username}, Token generated")
                    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Error creating user or token: {e}")
                return Response({"error": "Something went wrong during user creation"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger.warning("Creating new user failed due to validation errors")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
      authentication_classes = []
      permission_classes = []

      @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password']
        ),
   
    )

      def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            logger.info(f"Attempting to sign user in: {username}")

            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    logger.warning(f"Invalid password for username: {username}")
                    return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializer(user)
                logger.info(f"User signed in successfully: {username}")
                return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                logger.warning(f"User does not exist: {username}")
                return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        
        logger.warning("Username and password are required")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                            
                     
              
       
                
