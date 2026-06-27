import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def generate_synthetic_data(n_samples: int = 1200) -> pd.DataFrame:
    """Generate realistic synthetic MSME data"""
    np.random.seed(42)
    
    data = {
        'user_id': range(1, n_samples + 1),
        'monthly_income': np.random.lognormal(9, 0.8, n_samples).astype(int),
        'transaction_frequency': np.random.poisson(12, n_samples),
        'avg_loan_size': np.random.lognormal(10, 0.7, n_samples).astype(int),
        'savings_rate': np.random.beta(3, 7, n_samples),
        'digital_literacy_score': np.random.normal(65, 15, n_samples).clip(20, 95),
        'chatbot_sessions': np.random.poisson(8, n_samples),
        'response_time_sec': np.random.normal(45, 20, n_samples).clip(10, 120),
        'engagement_score': np.random.beta(4, 6, n_samples),
        'region': np.random.choice(['Nairobi', 'Mombasa', 'Kisumu', 'Rural'], n_samples, p=[0.35, 0.25, 0.2, 0.2]),
        'business_type': np.random.choice(['Retail', 'Agriculture', 'Services', 'Manufacturing'], n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Add some correlations
    df['savings_rate'] = df['savings_rate'] * (df['monthly_income'] / df['monthly_income'].max())
    df['engagement_score'] = (df['engagement_score'] + 0.3 * (df['digital_literacy_score']/100)).clip(0, 1)
    
    return df

def preprocess_data(df: pd.DataFrame):
    """Scale numeric features"""
    numeric_cols = ['monthly_income', 'transaction_frequency', 'avg_loan_size',
                    'savings_rate', 'digital_literacy_score', 'chatbot_sessions',
                    'response_time_sec', 'engagement_score']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[numeric_cols])
    return X_scaled, numeric_cols, scaler