package com.example.cvd_monitoring.di

import com.example.cvd_monitoring.data.CvdApi
import com.example.cvd_monitoring.data.repository.PatientRepositoryImpl
import com.example.cvd_monitoring.domain.repository.PatientRepository
import com.example.cvd_monitoring.utils.Constants
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object AppModule {

    @Provides
    @Singleton
    fun provideCvdAPi(): CvdApi {
        return Retrofit.Builder()
            .baseUrl(Constants.BASE_URI)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(CvdApi::class.java)
    }

    @Provides
    @Singleton
    fun providePatientRepository(api: CvdApi): PatientRepository = PatientRepositoryImpl(api)
}