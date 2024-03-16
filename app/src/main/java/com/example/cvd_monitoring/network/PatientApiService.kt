package com.example.cvd_monitoring.network

import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.utils.Constants
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface PatientApiService {

    @GET("users/v1/patients")
    suspend fun getPatientList(): List<Patient>

    @POST("users/v1/patients/registration")
    suspend fun createPatient(@Body patient: CreateUserRequest): User

    @POST("auth/v1/authenticate")
    suspend fun authenticateUser(@Body auth: Auth): Auth

    companion object {
        var apiService: PatientApiService? = null
        fun getInstance() : PatientApiService {
            if (apiService == null) {
                apiService = Retrofit.Builder()
                    .baseUrl(Constants.BASE_URI)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build().create(PatientApiService::class.java)
            }
            return apiService!!
        }
    }
}